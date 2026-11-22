from __future__ import annotations


def slugify(title: str) -> str:
    return title.lower().replace(" ", "-")


def is_valid_priority(value: int) -> bool:
    return 1 <= value <= 5
