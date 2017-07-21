"""Settings
"""
from django.conf import settings

if not settings.configured:
    settings.configure()

# GridFS
GRIDFS_TSNE_COLLECTION = getattr(settings, 'GRIDFS_TSNE_COLLECTION', 'fs_tsne')
