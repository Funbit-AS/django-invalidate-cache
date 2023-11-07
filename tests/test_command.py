import pytest
from django.core.management import CommandError, call_command

pytest.mark.django_db


def test_success(mock_myserver, capfd):
    # When:
    call_command("invalidate_cache", "pages")
    out, err = capfd.readouterr()
    assert out == "Successfully invalidated cache for tag pages\n"
    assert err == ""


def test_error(mock_myserver, capfd):
    # Given:
    mock_myserver.post("https://myserver.com/invalidate-cache/", status_code=400)
    # When:
    with pytest.raises(CommandError):
        call_command("invalidate_cache", "pages")
    out, err = capfd.readouterr()
    assert out == ""
    assert err == ""
