from __future__ import annotations

from src.services.billing import verify_account_status


def test_verify_account_status() -> None:
    if not verify_account_status(101):
        raise ValueError("Active account validation failed")
    if verify_account_status(-5):
        raise ValueError("Negative account validation failed")


test_verify_account_status()
