
<a id='changelog-1.0.1'></a>
# 1.0.1 — 2023-11-07

## Added

- `invalidate_tag` method now accepts a `fails_silently` flag which prevents exception being raised. Note that an error message is still logged.
- docstring for `invalidate_tag`

- Adds `InvalidateTagError` and `invalidate_tag` as top level package imports.

<a id='changelog-1.0.0'></a>
# 1.0.0 — 2023-11-07

## Added

- Management command `invalidate_cache <tag>`
- Wagtail admin view for manually invalidating tags
