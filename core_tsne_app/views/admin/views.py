"""T-SNE application admin views
"""
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
            tsne_api.upsert(tsne_map)
            # TODO: redirect
    # method is GET
    else:
        # render the form to upload a template
        context['upload_form'] = UploadMapForm()

    return admin_render(request,
                        'core_tsne_app/admin/map_upload.html',
                        assets=assets,
                        context=context,
                        modals=modals)
