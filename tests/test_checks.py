import pytest
from django.core.checks import Error
from django.core.checks.registry import CheckRegistry

pytestmark = pytest.mark.django_db


def test_error_picked_up_when_settings_missing(settings):
    # Given:
    del settings.DJANGO_CACHE_INVALIDATOR

    with pytest.raises(AttributeError):
        settings.DJANGO_CACHE_INVALIDATOR

    from invalidatecache.checks import check_settings

    registry = CheckRegistry()
    registry.register(check_settings)
    print(f"{registry.registered_checks=}")
    errors = registry.run_checks()

    assert errors == [
        Error(
            "DJANGO_CACHE_INVALIDATOR is not configured in settings",
            hint="Add DJANGO_CACHE_INVALIDATOR to settings",
            id="cacheinvalidator.E001",
        )
    ]
