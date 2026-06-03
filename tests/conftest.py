import pytest

@pytest.fixture(autouse=True)
def reset_mocks():
    """Reset any global mock state between tests."""
    from src.api.main import GlobalLedger
    GlobalLedger._entries.clear()
    yield
