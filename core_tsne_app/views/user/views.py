"""T-SNE application user views
"""
from core_main_app.utils.rendering import render


def tsne_map(request):
    """ Page that displays the T-SNE map.

    Args:
        request:

    Returns:

    """
    assets = {
        "js": [
            {
                "path": "core_tsne_app/js/user/map.plotly.js",
                "is_raw": False
            }
        ],
    }

    context = {

    }

    return render(request,
                  'core_tsne_app/user/index.html',
                  assets=assets,
                  context=context)


def tsne_map_from_data(request, data_id):
    """ Page that displays the T-SNE map, with a data selected

    Args:
        request:
        data_id:

    Returns:

    """
    assets = {
        "js": [
            {
                "path": "core_tsne_app/js/user/map.plotly.js",
                "is_raw": False
            }
        ],
    }

    context = {
        'data_id': data_id,
    }

    return render(request,
                  'core_tsne_app/user/index.html',
                  assets=assets,
                  context=context)
