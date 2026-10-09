import pytest
from src.services.billing import calculate_user_risk_profile

def test_calculate_user_risk_profile():
    result = calculate_user_risk_profile(
        balance=5000.0,
        failed_logins=0,
        is_verified=True,
        account_age_days=100,
        transaction_count=10,
    )
    assert result == 50.0
