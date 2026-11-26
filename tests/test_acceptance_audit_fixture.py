from acceptance_audit_fixture import (
    compliant_summary,
    covered_helper,
    well_documented_helper,
)


def test_acceptance_negative_controls():
    assert covered_helper(4) == 8
    assert well_documented_helper(7) == "task-7"
    assert compliant_summary([1, 2, 3], limit=2) == 3
