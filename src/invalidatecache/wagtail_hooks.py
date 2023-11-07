from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import ManualCacheInvalidationView


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(
            "manual-cache-invalidation/",
            ManualCacheInvalidationView.as_view(),
            name="manual-cache-invalidation",
        )
    ]


class ManualCache_invalidationMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register("register_settings_menu_item")
def register_manual_cache_invalidation_menu_item():
    return ManualCache_invalidationMenuItem(
        "Manually invalidate cache",
        url=reverse("manual-cache-invalidation"),
        classnames="icon icon-bin",
        order=10000,
    )
