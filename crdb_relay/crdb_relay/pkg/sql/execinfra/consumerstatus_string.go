// Code generated by "stringer"; DO NOT EDIT.

package execinfra

import "strconv"

func _() {
	// An "invalid array index" compiler error signifies that the constant values have changed.
	// Re-run the stringer command to generate them again.
	var x [1]struct{}
	_ = x[NeedMoreRows-0]
	_ = x[SwitchToAnotherPortal-1]
	_ = x[DrainRequested-2]
	_ = x[ConsumerClosed-3]
}

func (i ConsumerStatus) String() string {
	switch i {
	case NeedMoreRows:
		return "NeedMoreRows"
	case SwitchToAnotherPortal:
		return "SwitchToAnotherPortal"
	case DrainRequested:
		return "DrainRequested"
	case ConsumerClosed:
		return "ConsumerClosed"
	default:
		return "ConsumerStatus(" + strconv.FormatInt(int64(i), 10) + ")"
	}
}