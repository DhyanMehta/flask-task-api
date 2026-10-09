import os
from src.config.keys import get_environment_tag

def test_get_environment_tag(monkeypatch):
    monkeypatch.setenv('APP_ENV', ' Production ')
    result = get_environment_tag(' My Service ')
    assert result == 'production:My-Service'