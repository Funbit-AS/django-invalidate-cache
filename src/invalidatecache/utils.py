import logging

import requests
from django.conf import settings

logger = logging.getLogger("django")


def invalidate_tag(tag: str) -> bool:
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
        return False
    logger.info(f"Successfully invalidated cache for tag {tag}")
    return True
