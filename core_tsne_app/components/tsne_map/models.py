"""T-SNE Map model
"""
from django_mongoengine import fields, Document

from core_main_app.commons.exceptions import ModelError
from core_tsne_app.settings import GRIDFS_TSNE_COLLECTION

from mongoengine import errors as mongoengine_errors
from core_main_app.commons import exceptions
from core_tsne_app.utils.csv_operations import check_headers

CSV_HEADERS = ['X', 'Y', 'title', 'id']


class TSNEMap(Document):
    """T-SNE map class
    """
    file = fields.FileField(blank=False, collection_name=GRIDFS_TSNE_COLLECTION)

    @staticmethod
    def get_by_id(tsne_map_id):
        """ Return the object with the given id.

        Args:
            tsne_map_id:

        Returns:
            Data (obj): T-SNE map with the given id

        """
        try:
            return TSNEMap.objects.get(pk=str(tsne_map_id))
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(e.message)
        except Exception as ex:
            raise exceptions.ModelError(ex.message)

    @staticmethod
    def get_last():
        """ Return latest T-SNE map

        Returns:

        """
        # TODO: need testing
        return TSNEMap.objects().latest('id')

    def clean(self):
        """ Clean is called before saving

        Returns:

        """
        # read csv content
        csv_content = self.file.read()

        if not check_headers(csv_content, CSV_HEADERS):
            raise ModelError("Expected CSV file should have the following headers: {}".format(','.join(CSV_HEADERS)))
