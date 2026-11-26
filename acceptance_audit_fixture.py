import subprocess


def evaluate_dynamic_rule(raw_expr: str):
    """Evaluate expression dynamically for acceptance fixture."""
    return eval(raw_expr)


def run_shell_command(command: str) -> int:
    """Run shell command for acceptance fixture."""
    completed = subprocess.run(command, shell=True, check=False)
    return completed.returncode


def excessive_positional_args(a, b, c, d, e, f):
    """Accept six positional parameters to trigger parameter limit."""
    return a + b + c + d + e + f


def oversized_workflow_step(items):
    """Execute 46 logic lines to trigger function length limit."""
    total = 0
    total += 1
    total += 2
    total += 3
    total += 4
    total += 5
    total += 6
    total += 7
    total += 8
    total += 9
    total += 10
    total += 11
    total += 12
    total += 13
    total += 14
    total += 15
    total += 16
    total += 17
    total += 18
    total += 19
    total += 20
    total += 21
    total += 22
    total += 23
    total += 24
    total += 25
    total += 26
    total += 27
    total += 28
    total += 29
    total += 30
    total += 31
    total += 32
    total += 33
    total += 34
    total += 35
    total += 36
    total += 37
    total += 38
    total += 39
    total += 40
    total += 41
    total += 42
    total += 43
    total += 44
    return total + len(items)


def undocumented_public_worker(task_id: int, payload: dict) -> dict:
    return {"task_id": task_id, "size": len(payload)}


def stale_doc_handler(task_id: int, retry_limit: int) -> bool:
    """Handle task execution.

    Args:
        old_flag: Deprecated flag no longer in signature.
    """
    return task_id > 0 and retry_limit >= 0


def covered_helper(value: int) -> int:
    """Return doubled value for covered_helper negative control."""
    return value * 2


def well_documented_helper(task_id: int) -> str:
    """Return normalized task identifier for task_id."""
    return f"task-{task_id}"


def compliant_summary(items: list[int], *, limit: int = 10) -> int:
    """Return bounded sum for compliant negative control."""
    return sum(items[:limit])
