""" Url router for the T-SNE application
"""
from django.conf.urls import url, include
from core_tsne_app.views.user import views as user_views

urlpatterns = [
    url(r'^$', user_views.tsne_map,
        name='core_tsne_app_index'),
    url(r'^data/(?P<data_id>\w+)$', user_views.tsne_map_from_data,
        name='core_tsne_app_data'),
    url(r'^rest/', include('core_tsne_app.rest.urls')),
]
