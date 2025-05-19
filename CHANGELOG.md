
<a id='changelog-1.0.3'></a>
# 1.0.3 — 2025-05-19

## Changed

- Changed `classnames` to `classname` to support `wagtail 7.0`

<a id='changelog-1.0.2'></a>
# 1.0.2 — 2023-11-15

## Fixed

- Adds html files to package data.

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
