# core_tsne_app

core_tsne_app is a Django app.

# Quick start

1. Add "core_tsne_app" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    "core_tsne_app",
]
```

2. Include the core_tsne_app URLconf in your project urls.py like this::

```python
url(r'^tsne/', include("core_tsne_app.urls")),
```