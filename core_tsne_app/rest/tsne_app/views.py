"""T-SNE application rest views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core_main_app.commons import exceptions
from core_main_app.utils.file import get_file_http_response

from core_tsne_app.components.tsne_map import api as tsne_map_api


@api_view(['GET'])
def download_latest(request):
    """Download the map file.

    /rest/tsne/map/download/latest

    Args:
        request:

    Returns:

    """
    try:
        # get T-SNE map
        tsne_map = tsne_map_api.get_last(request.user)
        # return csv file
        return get_file_http_response(tsne_map, 'tsne_app', extension='csv')
    except exceptions.DoesNotExist as e:
        content = {'message': 'No data found with the given id.'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    except Exception as api_exception:
        content = {'message': api_exception.message}
        return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
