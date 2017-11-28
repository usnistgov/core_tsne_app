"""Url router for the administration site
"""
from django.contrib import admin
from django.conf.urls import url

from core_tsne_app.views.admin import views as admin_views


admin_urls = [
    url(r'^map/upload$', admin_views.upload_map,
        name='core_tsne_app_upload_map'),
]

urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
