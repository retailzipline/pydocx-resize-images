import collections
import collections.abc


# PyDocX 0.9.10 imports Hashable from collections. Python 3.12 only exposes
# abstract base classes from collections.abc, so retain the name that PyDocX
# expects until it adopts the modern import itself.
if not hasattr(collections, 'Hashable'):
    collections.Hashable = collections.abc.Hashable

from .mixins.image_resize import ResizedImagesExportMixin

__all__ = [
    'ResizedImagesExportMixin'
]

__version__ = '0.0.3'
