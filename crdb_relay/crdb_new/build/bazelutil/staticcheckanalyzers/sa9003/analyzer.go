// Code generated by generate-staticcheck; DO NOT EDIT.

//go:build bazel
// +build bazel

package sa9003

import (
	util "github.com/cockroachdb/cockroach/pkg/testutils/lint/passes/staticcheck"
	"golang.org/x/tools/go/analysis"
	"honnef.co/go/tools/staticcheck"
)

var Analyzer *analysis.Analyzer

func init() {
	for _, analyzer := range staticcheck.Analyzers {
		if analyzer.Analyzer.Name == "SA9003" {
			Analyzer = analyzer.Analyzer
			break
		}
	}
	util.MungeAnalyzer(Analyzer)
}
