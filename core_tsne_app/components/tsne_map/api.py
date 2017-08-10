"""T-SNE map api
"""
from core_tsne_app.components.tsne_map.models import TSNEMap
from core_main_app.components.data import api as data_api
from core_tsne_app.utils.csv_operations import filter_rows


def upsert(tsne_map):
    """ Save or update a T-SNE map.

    Args:
        map:

    Returns:

    """
    return tsne_map.save()


def get_last(user):
    """ Return last T-SNE map.

    Returns:

    """
    # Get latest T-SNE map
    tsne_map = TSNEMap.get_last()
    # Get ids of accessible data
    accessible_data = map(str, data_api.execute_query({}, user).values_list('id'))
    # read csv content
    csv_content = tsne_map.file.read()
    # filter csv content, keeping only accessible data
    filtered_csv_content = filter_rows(csv_content, column_index=-1, allowed_values=accessible_data)

    return filtered_csv_content
