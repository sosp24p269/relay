// Code generated by "stringer"; DO NOT EDIT.

package sctest

import "strconv"

func _() {
	// An "invalid array index" compiler error signifies that the constant values have changed.
	// Re-run the stringer command to generate them again.
	var x [1]struct{}
	_ = x[stageExecuteQuery-1]
	_ = x[stageExecuteStmt-2]
}

func (i stageExecType) String() string {
	switch i {
	case stageExecuteQuery:
		return "stageExecuteQuery"
	case stageExecuteStmt:
		return "stageExecuteStmt"
	default:
		return "stageExecType(" + strconv.FormatInt(int64(i), 10) + ")"
	}
}
