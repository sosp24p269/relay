// Copyright 2021 The Cockroach Authors.
//
// Use of this software is governed by the Business Source License
// included in the file licenses/BSL.txt.
//
// As of the Change Date specified in that file, in accordance with
// the Business Source License, use of this software will be governed
// by the Apache License, Version 2.0, included in the file
// licenses/APL.txt.

//go:build generator
// +build generator

package main

import (
	"bytes"
	"flag"
	"fmt"
	"os"
	"regexp"
	"sort"
	"text/template"

	"github.com/cockroachdb/cockroach/pkg/cli/exit"
)

var (
	in  = flag.String("in", "", "input proto file")
	out = flag.String("out", "", "output file for generated go code")
)

func main() {
	flag.Parse()
	if err := run(*in, *out); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		exit.WithCode(exit.FatalError())
	}
}

func run(in, out string) error {
	if out == "" {
		return fmt.Errorf("output required")
	}
	elementNames, err := getElementNames(in)
	if err != nil {
		return err
	}
	var buf bytes.Buffer
	if err := template.Must(template.New("templ").Parse(`{{- /**/ -}}
// Copyright 2021 The Cockroach Authors.
//
// Use of this software is governed by the Business Source License
// included in the file licenses/BSL.txt.
//
// As of the Change Date specified in that file, in accordance with
// the Business Source License, use of this software will be governed
// by the Apache License, Version 2.0, included in the file
// licenses/APL.txt.

// Code generated by element_generator.go. DO NOT EDIT.

package scpb

import "fmt"
{{ range . }}

func (e {{ . }}) element() {}

// Element implements ElementGetter.
func (e * ElementProto_{{ . }}) Element() Element {
	return e.{{ . }}
}

// ForEach{{ . }} iterates over elements of type {{ . }}.
// Deprecated
func ForEach{{ . }}(
	c *ElementCollection[Element], fn func(current Status, target TargetStatus, e *{{ . }}),
) {
  c.Filter{{ . }}().ForEach(fn)
}

// Find{{ . }} finds the first element of type {{ . }}.
// Deprecated
func Find{{ . }}(
	c *ElementCollection[Element],
) (current Status, target TargetStatus, element *{{ . }}) {
	if tc := c.Filter{{ . }}(); !tc.IsEmpty() {
		var e Element
		current, target, e = tc.Get(0)
		element = e.(*{{ . }})
	}
	return current, target, element
}

// {{ . }}Elements filters elements of type {{ . }}.
func (c *ElementCollection[E]) Filter{{ . }}() *ElementCollection[*{{ . }}] {
	ret := c.genericFilter(func(_ Status, _ TargetStatus, e Element) bool {
		_, ok := e.(*{{ . }})
		return ok
	})
	return (*ElementCollection[*{{ . }}])(ret)
}

{{- end -}}
//
// SetElements sets the element inside the protobuf.
func (e* ElementProto) SetElement(element Element) {
	switch t := element.(type) {
		default:
			panic(fmt.Sprintf("unknown type %T", t))
{{ range . }}
		case *{{ . }}:
			e.ElementOneOf = &ElementProto_{{ . }}{ {{ . }}: t}
{{- end -}}
	}
}
//
// GetElementOneOfProtos returns all one of protos.
func GetElementOneOfProtos() []interface{} {
	return []interface{} {
{{ range . }}
	((*ElementProto_{{ . }})(nil)),
{{- end -}}
	}
}
//
// GetElementTypes returns all element types. 
func GetElementTypes() []interface{} {

	return []interface{} {
{{ range . }}
	((*{{ . }})(nil)),
{{- end -}}
}
}
//
// ForEachElementType loops over each element type
func ForEachElementType(fn func(e Element) error) error {
	for _, e := range GetElementTypes() {
		if err := fn(e.(Element)); err != nil {
			return err
		}
	}
	return nil
}
`)).Execute(&buf, elementNames); err != nil {
		return err
	}
	return os.WriteFile(out, buf.Bytes(), 0777)
}

// getElementNames parses the ElementsProto struct definition and extracts
// the names of the types of its members.
func getElementNames(inProtoFile string) (names []string, _ error) {
	var (
		// e.g.: (gogoproto.customname) = 'field'
		elementProtoBufMetaField = `\([A-z\.]+\)\s+=\s+\"[A-z\:\",\s]+`
		// e.g.: [ (gogoproto.a) = b, (gogoproto.customname) = 'c' ]
		elementProtoBufMeta = `(\s+\[(` + elementProtoBufMetaField + `)*\](\s+,\s+(` + elementProtoBufMetaField + `))*)?`
		elementFieldPat     = `\s*(?P<type>\w+)\s+(?P<name>\w+)\s+=\s+\d+` +
			elementProtoBufMeta + `;`
		elementProtoRegexp = regexp.MustCompile(`(?s)message ElementProto {
  oneof element_one_of {
(?P<fields>(` + elementFieldPat + "\n)+)" +
			"\\s*}",
		)
		elementFieldRegexp  = regexp.MustCompile(elementFieldPat)
		elementFieldTypeIdx = elementFieldRegexp.SubexpIndex("type")
		elementFieldsIdx    = elementProtoRegexp.SubexpIndex("fields")
		commentPat          = "\\/\\/[^\n]*\n"
		commentRegexp       = regexp.MustCompile(commentPat)
	)

	got, err := os.ReadFile(inProtoFile)
	got = commentRegexp.ReplaceAll(got, nil)

	if err != nil {
		return nil, err
	}
	submatch := elementProtoRegexp.FindSubmatch(got)
	if submatch == nil {
		return nil, fmt.Errorf(""+
			"failed to find ElementProto in %s: %s",
			inProtoFile, elementProtoRegexp)
	}
	fieldMatches := elementFieldRegexp.FindAllSubmatch(submatch[elementFieldsIdx], -1)
	for _, m := range fieldMatches {
		names = append(names, string(m[elementFieldTypeIdx]))
	}
	sort.Strings(names)
	return names, nil
}