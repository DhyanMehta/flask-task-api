import pytest
from src.services.billing import calculate_user_risk_profile

def test_calculate_user_risk_profile():
    result = calculate_user_risk_profile(
        balance=150000.0,
        failed_logins=0,
        is_verified=True,
        account_age_days=400,
        transaction_count=500,
    )
    assert result == pytest.approx(46.75)
