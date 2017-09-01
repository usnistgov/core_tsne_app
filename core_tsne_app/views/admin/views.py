"""T-SNE application admin views
"""
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

from core_main_app.commons.exceptions import ModelError
from core_main_app.utils.rendering import admin_render
from core_tsne_app.components.tsne_map.models import TSNEMap
from core_tsne_app.components.tsne_map import api as tsne_api
from core_tsne_app.views.admin.forms import UploadMapForm


def upload_map(request):
    """Upload type.

    Args:
        request:

    Returns:

    """
    assets = {}
    context = {'object_name': 'T-SNE Map'}
    modals = []

    # method is POST
    if request.method == 'POST':
        form = UploadMapForm(request.POST, request.FILES)
        context['upload_form'] = form

        if form.is_valid():
            tsne_map = TSNEMap(file=request.FILES['file'])
            try:
                tsne_api.upsert(tsne_map)
                return HttpResponseRedirect(reverse("admin:core_main_app_admin_home"))
            except ModelError, e:
                form.add_error('file', e.message)
    # method is GET
    else:
        # render the form to upload a template
        context['upload_form'] = UploadMapForm()

    return admin_render(request,
                        'core_tsne_app/admin/map_upload.html',
                        assets=assets,
                        context=context,
                        modals=modals)
