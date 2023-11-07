# Django Invalidate Cache

Helpers for sending invalidate requests to a http endpoint (such as a nextjs api route).

## Usage

### Signals

Setup automatically cache invalidation of django/wagtail models by adding signal handlers:

```python
def register_signal_handlers():
    # Connect for all page types by not specifying sender
    page_published.connect(signal_handler, dispatch_uid="cache_invalidator")
    page_unpublished.connect(signal_handler, dispatch_uid="cache_invalidator")
    post_page_move.connect(signal_handler, dispatch_uid="cache_invalidator")

    # Invalidate other models that use page data
    for app, model in [
        ("app1", "FirstModel"),
        ("app1", "SecondModel"),
        ("app2", "ThirdModel"),
    ]:
        Model = apps.get_model(app, model)
        post_save.connect(signal_handler, sender=Model)
        post_delete.connect(signal_handler, sender=Model)


def signal_handler(sender, instance, **kwargs):
    invalidate_cache(tag="pages", fail_silently=True)
```

### Management Command

Run `python manage.py invalidate_tag <tag>` to invalidate a tag.

### Admin view

There is a wagtail admin view, added to the settings menu, for manually invalidating a tag.

## Releasing a new version

### Preparation

1. Update version number in `pyproject.toml`
2. Use `scriv create` to add to changelog

### Release

- Run `make release`
