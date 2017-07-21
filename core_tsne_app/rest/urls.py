"""Url router for the REST API
"""
from django.conf.urls import url
from core_tsne_app.rest.tsne_app import views as tsne_views

urlpatterns = [
    url(r'^map/download/latest', tsne_views.download_latest,
        name='core_tsne_app_rest_map_download_latest'),
]
