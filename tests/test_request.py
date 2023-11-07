import pytest
from requests.exceptions import ConnectionError, HTTPError, Timeout

from invalidatecache.utils import invalidate_tag


def test_outgoing_request(settings, mock_myserver):
    # Given:
    assert settings.DJANGO_CACHE_INVALIDATOR == {
        "URL": "https://myserver.com/invalidate-cache/",
        "SECRET": "mysecret",
    }

    # When:
    invalidate_tag("pages")

    # Then:
    assert len(mock_myserver.request_history) == 1
    request = mock_myserver.request_history[0]
    assert request.method == "POST"
    assert request.url == "https://myserver.com/invalidate-cache/?tag=pages"
    assert "Authorization" in request.headers
    auth = request.headers["Authorization"]
    assert auth == "Bearer mysecret"


def test_invalidate_tag_success(settings, mock_myserver):
    result = invalidate_tag("test_tag")
    assert result is True


def test_invalidate_tag_400(settings, mock_myserver):
    mock_myserver.post("https://myserver.com/invalidate-cache/", status_code=400)

    result = invalidate_tag("test_tag")
    assert result is False


@pytest.mark.parametrize("exception", [HTTPError, Timeout, ConnectionError])
def test_invalidate_tag_failure(settings, mock_myserver, exception):
    mock_myserver.post("https://myserver.com/invalidate-cache/", exc=exception)
    result = invalidate_tag("test_tag")

    assert result is False
