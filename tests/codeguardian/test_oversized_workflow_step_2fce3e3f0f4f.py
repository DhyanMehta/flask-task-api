import pytest
from acceptance_audit_fixture import oversized_workflow_step

def test_oversized_workflow_step():
    items = [1, 2, 3]
    assert oversized_workflow_step(items) == 990 + len(items)