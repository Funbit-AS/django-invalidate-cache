import pytest


@pytest.fixture(autouse=True)
def mock_myserver(requests_mock):
    requests_mock.post("https://myserver.com/invalidate-cache/", status_code=200)
    yield requests_mock
