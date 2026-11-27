import subprocess
from acceptance_audit_fixture import run_shell_command

def test_run_shell_command():
    # Use a simple command that always succeeds
    assert run_shell_command('true') == 0
