import logging

import requests
from django.conf import settings
from requests.exceptions import RequestException

logger = logging.getLogger("django")


class InvalidateTagError(RequestException):
    """Exception raised when the request to invalidate a tag fails."""

    pass


def invalidate_tag(tag: str, fail_silently=False):
    """
    Invalidate a cache tag.

    This function sends a POST request to a specified URL to invalidate a cache tag.
    If the request fails, it logs the error and raises an InvalidateTagError unless
    fail_silently is True.

    Parameters:
    tag (str): The cache tag to invalidate.
    fail_silently (bool): Whether to suppress exceptions and only log an error.

    Raises:
    InvalidateTagError: If the request fails and fail_silently is False.
    """
    cache_settings = getattr(settings, "DJANGO_CACHE_INVALIDATOR", {})
    url = cache_settings.get("URL", "")
    secret = cache_settings.get("SECRET", "")

    try:
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {secret}"},
            params={"tag": tag},
            timeout=5,
        )
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error invalidating cache for tag {tag}: {e}")
        if not fail_silently:
            raise InvalidateTagError() from e

    else:
        logger.info(f"Successfully invalidated cache for tag {tag}")
