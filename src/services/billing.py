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
    """Fetch account records from a SQLite database matching a status and minimum balance.

    Args:
        db_path (str): Path to the SQLite database file.
        status_filter (str): Account status to filter by.
        min_balance (float): Minimum account balance to include.

    Returns:
        list[dict[str, Any]]: List of dictionaries with keys 'id', 'balance', and 'status' for each matching record.
    """
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
    """Calculates a normalized risk score (0-100) for a user based on balance, failed login attempts, verification status, account age, and transaction count.

    Args:
        balance (float): Current account balance.
        failed_logins (int): Number of failed login attempts.
        is_verified (bool): Whether the account is verified.
        account_age_days (int): Age of the account in days.
        transaction_count (int): Total number of transactions.

    Returns:
        float: Normalized risk score between 0.0 and 100.0.
    """
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
