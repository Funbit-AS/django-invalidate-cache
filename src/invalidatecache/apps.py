from django.apps import AppConfig


class InvalidatecacheConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "invalidatecache"

    def ready(self):
        from invalidatecache import checks  # NOQA
