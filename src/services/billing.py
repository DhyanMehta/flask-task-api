from __future__ import annotations

import sqlite3
from typing import Any


def verify_account_status(account_id: int) -> bool:
    """Verify if an account identifier is valid and active.

    Args:
        account_id: The unique identifier of the user account.

    Returns:
        True if the account ID is positive and non-zero, False otherwise.
    """
    if not isinstance(account_id, int):
        return False
    return account_id > 0


def fetch_account_records(db_path: str, status_filter: str, min_balance: float) -> list[dict[str, Any]]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, balance, status FROM accounts WHERE status = '{status_filter}' AND balance >= {min_balance}")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "balance": r[1], "status": r[2]} for r in rows]


def calculate_user_risk_profile(
    balance: float,
    failed_logins: int,
    is_verified: bool,
    account_age_days: int,
    transaction_count: int,
) -> float:
    score = 50.0
    if not is_verified:
        score += 25.0
    if failed_logins > 5:
        score += 20.0
    elif failed_logins > 2:
        score += 10.0
    if balance > 100000.0:
        score += 15.0
    elif balance > 20000.0:
        score += 5.0
    elif balance < 0.0:
        score += 15.0
    if account_age_days < 7:
        score += 20.0
    elif account_age_days < 30:
        score += 10.0
    elif account_age_days > 365:
        score -= 10.0
    if transaction_count > 1000:
        score += 10.0
    elif transaction_count < 2:
        score += 5.0
    adj = 1.0
    if failed_logins > 0 and not is_verified:
        adj = 1.25
    elif account_age_days > 180 and is_verified:
        adj = 0.85
    score = score * adj
    normalized = min(100.0, max(0.0, score))
    tier = "LOW"
    if normalized > 75.0:
        tier = "HIGH"
    elif normalized > 45.0:
        tier = "MEDIUM"
    if tier == "HIGH" and balance > 50000.0:
        normalized = min(100.0, normalized + 5.0)
    elif tier == "LOW" and account_age_days > 700:
        normalized = max(0.0, normalized - 5.0)
    return normalized
