from django.conf import settings
from django.core.checks import Error, Tags, register


@register(Tags.compatibility)
def check_settings(app_configs, **kwargs):
    try:
        settings.DJANGO_CACHE_INVALIDATOR
    except AttributeError:
        return [
            Error(
                "DJANGO_CACHE_INVALIDATOR is not configured in settings",
                hint="Add DJANGO_CACHE_INVALIDATOR to settings",
                id="cacheinvalidator.E001",
            )
        ]
    return []
