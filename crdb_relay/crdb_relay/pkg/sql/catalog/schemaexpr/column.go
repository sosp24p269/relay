// Copyright 2020 The Cockroach Authors.
//
// Use of this software is governed by the Business Source License
// included in the file licenses/BSL.txt.
//
// As of the Change Date specified in that file, in accordance with
// the Business Source License, use of this software will be governed
// by the Apache License, Version 2.0, included in the file
// licenses/APL.txt.

package schemaexpr

import (
	"context"
	"fmt"

	"github.com/cockroachdb/cockroach/pkg/sql/catalog"
	"github.com/cockroachdb/cockroach/pkg/sql/catalog/colinfo"
	"github.com/cockroachdb/cockroach/pkg/sql/parser"
	"github.com/cockroachdb/cockroach/pkg/sql/pgwire/pgcode"
	"github.com/cockroachdb/cockroach/pkg/sql/pgwire/pgerror"
	"github.com/cockroachdb/cockroach/pkg/sql/sem/catid"
	"github.com/cockroachdb/cockroach/pkg/sql/sem/tree"
	"github.com/cockroachdb/cockroach/pkg/sql/sessiondata"
	"github.com/cockroachdb/cockroach/pkg/sql/types"
)

// DequalifyColumnRefs returns a serialized expression with database and table
// names stripped from qualified column names.
//
// For example:
//
//	tab.a > 0 AND db.tab.b = 'foo'
//	=>
//	a > 0 AND b = 'foo'
//
// This dequalification is necessary when CHECK constraints, computed columns,
// or partial index predicates are created. If the table name was not stripped,
// these expressions would become invalid if the table is renamed.
func DequalifyColumnRefs(
	ctx context.Context, source *colinfo.DataSourceInfo, expr tree.Expr,
) (string, error) {
	e, err := dequalifyColumnRefs(ctx, source, expr)
	if err != nil {
		return "", err
	}
	return tree.Serialize(e), nil
}

// dequalifyColumnRefs returns an expression with database and table names
// stripped from qualified column names.
func dequalifyColumnRefs(
	ctx context.Context, source *colinfo.DataSourceInfo, expr tree.Expr,
) (tree.Expr, error) {
	resolver := colinfo.ColumnResolver{Source: source}
	return tree.SimpleVisit(
		expr,
		func(expr tree.Expr) (recurse bool, newExpr tree.Expr, err error) {
			if vBase, ok := expr.(tree.VarName); ok {
				v, err := vBase.NormalizeVarName()
				if err != nil {
					return false, nil, err
				}
				if c, ok := v.(*tree.ColumnItem); ok {
					_, err := colinfo.ResolveColumnItem(ctx, &resolver, c)
					if err != nil {
						return false, nil, err
					}
					colIdx := resolver.ResolverState.ColIdx
					col := source.SourceColumns[colIdx]
					return false, &tree.ColumnItem{ColumnName: tree.Name(col.Name)}, nil
				}
			}
			return true, expr, err
		},
	)
}

// FormatColumnForDisplay formats a column descriptor as a SQL string. It
// converts user defined types in default and computed expressions to a
// human-readable form.
func FormatColumnForDisplay(
	ctx context.Context,
	tbl catalog.TableDescriptor,
	col catalog.Column,
	semaCtx *tree.SemaContext,
	sessionData *sessiondata.SessionData,
	redactableValues bool,
) (string, error) {
	f := tree.NewFmtCtx(tree.FmtSimple)
	name := col.GetName()
	f.FormatNameP(&name)
	f.WriteByte(' ')
	f.WriteString(col.GetType().SQLString())
	if col.IsHidden() {
		f.WriteString(" NOT VISIBLE")
	}
	if col.IsNullable() {
		f.WriteString(" NULL")
	} else {
		f.WriteString(" NOT NULL")
	}
	fmtFlags := tree.FmtParsable
	if redactableValues {
		fmtFlags |= tree.FmtMarkRedactionNode | tree.FmtOmitNameRedaction
	}
	if col.HasDefault() {
		if col.IsGeneratedAsIdentity() {
			if col.IsGeneratedAlwaysAsIdentity() {
				f.WriteString(" GENERATED ALWAYS AS IDENTITY")
			} else if col.IsGeneratedByDefaultAsIdentity() {
				f.WriteString(" GENERATED BY DEFAULT AS IDENTITY")
			}
			if col.HasGeneratedAsIdentitySequenceOption() {
				seqOpt := col.GetGeneratedAsIdentitySequenceOptionStr()
				s := formatGeneratedAsIdentitySequenceOption(seqOpt)
				f.WriteString(s)
			}

		} else {
			f.WriteString(" DEFAULT ")
			defExpr, err := FormatExprForDisplay(ctx, tbl, col.GetDefaultExpr(), semaCtx, sessionData, fmtFlags)
			if err != nil {
				return "", err
			}
			f.WriteString(defExpr)
		}
	}
	if col.HasOnUpdate() {
		f.WriteString(" ON UPDATE ")
		onUpdateExpr, err := FormatExprForDisplay(ctx, tbl, col.GetOnUpdateExpr(), semaCtx, sessionData, fmtFlags)
		if err != nil {
			return "", err
		}
		f.WriteString(onUpdateExpr)
	}
	if col.IsComputed() {
		f.WriteString(" AS (")
		compExpr, err := FormatExprForDisplay(ctx, tbl, col.GetComputeExpr(), semaCtx, sessionData, fmtFlags)
		if err != nil {
			return "", err
		}
		f.WriteString(compExpr)
		if col.IsVirtual() {
			f.WriteString(") VIRTUAL")
		} else {
			f.WriteString(") STORED")
		}
	}
	return f.CloseAndGetString(), nil
}

// RenameColumn replaces any occurrence of the column from in expr with to, and
// returns a string representation of the new expression.
func RenameColumn(expr string, from tree.Name, to tree.Name) (string, error) {
	parsed, err := parser.ParseExpr(expr)
	if err != nil {
		return "", err
	}

	replaceFn := func(expr tree.Expr) (recurse bool, newExpr tree.Expr, err error) {
		if vBase, ok := expr.(tree.VarName); ok {
			v, err := vBase.NormalizeVarName()
			if err != nil {
				return false, nil, err
			}
			if c, ok := v.(*tree.ColumnItem); ok {
				if string(c.ColumnName) == string(from) {
					c.ColumnName = to
				}
			}
			return false, v, nil
		}
		return true, expr, nil
	}

	renamed, err := tree.SimpleVisit(parsed, replaceFn)
	if err != nil {
		return "", err
	}

	return renamed.String(), nil
}

// iterColDescriptors iterates over the expression's variable columns and
// calls f on each.
//
// If the expression references a column that does not exist in the table
// descriptor, iterColDescriptors errs with pgcode.UndefinedColumn.
func iterColDescriptors(
	desc catalog.TableDescriptor, rootExpr tree.Expr, f func(column catalog.Column) error,
) error {
	_, err := tree.SimpleVisit(rootExpr, func(expr tree.Expr) (recurse bool, newExpr tree.Expr, err error) {
		vBase, ok := expr.(tree.VarName)
		if !ok {
			// Not a VarName, don't do anything to this node.
			return true, expr, nil
		}

		v, err := vBase.NormalizeVarName()
		if err != nil {
			return false, nil, err
		}

		c, ok := v.(*tree.ColumnItem)
		if !ok {
			return true, expr, nil
		}

		col, err := catalog.MustFindColumnByTreeName(desc, c.ColumnName)
		if err != nil || col.Dropped() {
			return false, nil, pgerror.Newf(pgcode.UndefinedColumn,
				"column %q does not exist, referenced in %q", c.ColumnName, rootExpr.String())
		}

		if err := f(col); err != nil {
			return false, nil, err
		}
		return false, expr, err
	})

	return err
}

// dummyColumn represents a variable column that can type-checked. It is used
// in validating check constraint and partial index predicate expressions. This
// validation requires that the expression can be both both typed-checked and
// examined for variable expressions.
type dummyColumn struct {
	typ  *types.T
	name tree.Name
}

// String implements the Stringer interface.
func (d *dummyColumn) String() string {
	return tree.AsString(d)
}

// Format implements the NodeFormatter interface.
func (d *dummyColumn) Format(ctx *tree.FmtCtx) {
	d.name.Format(ctx)
}

// Walk implements the Expr interface.
func (d *dummyColumn) Walk(_ tree.Visitor) tree.Expr {
	return d
}

// TypeCheck implements the Expr interface.
func (d *dummyColumn) TypeCheck(
	_ context.Context, _ *tree.SemaContext, desired *types.T,
) (tree.TypedExpr, error) {
	return d, nil
}

func (*dummyColumn) Eval(ctx context.Context, v tree.ExprEvaluator) (tree.Datum, error) {
	panic("dummyColumnItem.EvalVisit() is undefined")
}

// ResolvedType implements the TypedExpr interface.
func (d *dummyColumn) ResolvedType() *types.T {
	return d.typ
}

// ReplaceColumnVars replaces the occurrences of column names in an expression with
// dummyColumns containing their type, so that they may be type-checked. It
// returns this new expression tree alongside a set containing the ColumnID of
// each column seen in the expression.
//
// If the expression references a column that does not exist in the table
// descriptor, replaceColumnVars errs with pgcode.UndefinedColumn.
//
// The column lookup function allows looking up columns both in the descriptor
// or in declarative schema changer elements.
func ReplaceColumnVars(
	rootExpr tree.Expr,
	columnLookupFn func(columnName tree.Name) (exists bool, accessible bool, id catid.ColumnID, typ *types.T),
) (tree.Expr, catalog.TableColSet, error) {
	var colIDs catalog.TableColSet

	newExpr, err := tree.SimpleVisit(rootExpr, func(expr tree.Expr) (recurse bool, newExpr tree.Expr, err error) {
		vBase, ok := expr.(tree.VarName)
		if !ok {
			// Not a VarName, don't do anything to this node.
			return true, expr, nil
		}

		v, err := vBase.NormalizeVarName()
		if err != nil {
			return false, nil, err
		}

		c, ok := v.(*tree.ColumnItem)
		if !ok {
			return true, expr, nil
		}

		colExists, colIsAccessible, colID, colType := columnLookupFn(c.ColumnName)
		if !colExists {
			return false, nil, pgerror.Newf(pgcode.UndefinedColumn,
				"column %q does not exist, referenced in %q", c.ColumnName, rootExpr.String())
		}
		if !colIsAccessible {
			return false, nil, pgerror.Newf(pgcode.UndefinedColumn,
				"column %q is inaccessible and cannot be referenced", c.ColumnName)
		}
		colIDs.Add(colID)

		// Convert to a dummyColumn of the correct type.
		return false, &dummyColumn{typ: colType, name: c.ColumnName}, nil
	})

	return newExpr, colIDs, err
}

// replaceColumnVars is a convenience function for ReplaceColumnVars.
func replaceColumnVars(
	tbl catalog.TableDescriptor, rootExpr tree.Expr,
) (tree.Expr, catalog.TableColSet, error) {
	lookupFn := func(columnName tree.Name) (exists bool, accessible bool, id catid.ColumnID, typ *types.T) {
		col, err := catalog.MustFindColumnByTreeName(tbl, columnName)
		if err != nil || col.Dropped() {
			return false, false, 0, nil
		}
		return true, !col.IsInaccessible(), col.GetID(), col.GetType()
	}
	return ReplaceColumnVars(rootExpr, lookupFn)
}

// ReplaceSequenceIDsWithFQNames walks the given expr and replaces occurrences
// of regclass IDs in the expr with the descriptor's fully qualified name.
// For example, nextval(12345::REGCLASS) => nextval('foo.public.seq').
func ReplaceSequenceIDsWithFQNames(
	ctx context.Context, rootExpr tree.Expr, semaCtx *tree.SemaContext,
) (tree.Expr, error) {
	replaceFn := func(expr tree.Expr) (recurse bool, newExpr tree.Expr, err error) {
		id, ok := GetSeqIDFromExpr(expr)
		if !ok {
			return true, expr, nil
		}
		// If it's not a sequence or the resolution fails, skip this node.
		seqName, err := semaCtx.NameResolver.GetQualifiedTableNameByID(ctx, id, tree.ResolveRequireSequenceDesc)
		if err != nil {
			return true, expr, nil //nolint:returnerrcheck
		}

		// Omit the database qualification if the sequence lives in the current database.
		currDb := semaCtx.NameResolver.CurrentDatabase()
		if seqName.Catalog() == currDb {
			seqName.CatalogName = ""
			seqName.ExplicitCatalog = false
		}

		// Swap out this node to use the qualified table name for the sequence.
		return false, &tree.CastExpr{
			Type:       types.RegClass,
			SyntaxMode: tree.CastShort,
			Expr:       tree.NewStrVal(seqName.String()),
		}, nil
	}

	newExpr, err := tree.SimpleVisit(rootExpr, replaceFn)
	return newExpr, err
}

// GetSeqIDFromExpr takes an expr and looks for a sequence ID in
// this expr. If it finds one, it will return that ID.
func GetSeqIDFromExpr(expr tree.Expr) (int64, bool) {
	// Depending on if the given expr is typed checked, we're looking
	// for either a *tree.AnnotateTypeExpr (if not typed checked), or
	// a *tree.DOid (if type checked).
	switch n := expr.(type) {
	case *tree.AnnotateTypeExpr:
		if typ, safe := tree.GetStaticallyKnownType(n.Type); !safe || typ.Family() != types.OidFamily {
			return 0, false
		}
		numVal, ok := n.Expr.(*tree.NumVal)
		if !ok {
			return 0, false
		}
		id, err := numVal.AsInt64()
		if err != nil {
			return 0, false
		}
		return id, true
	case *tree.DOid:
		return int64(n.Oid), true
	default:
		return 0, false
	}
}

// formatGeneratedAsIdentitySequenceOption returns the formatted sequence option
// expression for GENERATED AS IDENTITY column.
func formatGeneratedAsIdentitySequenceOption(seqOpt string) string {
	if seqOpt == "" {
		return ""
	}
	return fmt.Sprintf(" (%s)", seqOpt)
}