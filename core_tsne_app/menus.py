""" Add T-SNE to main menu
"""
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item(
    "main", MenuItem("T-SNE", reverse("core_tsne_app_index"))
)

types_children = (
    MenuItem("Upload Map", reverse("admin:core_tsne_app_upload_map"), icon="upload"),
)

Menu.add_item(
    "admin", MenuItem("T-SNE", None, children=types_children)
)
