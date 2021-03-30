from pkg_resources import packaging

from .constants import DEFAULT_PROTOCOL
from .fields import PickledObjectField

__all__ = 'VERSION', '__version__', 'DEFAULT_PROTOCOL', 'PickledObjectField'

VERSION = (3, 0, 1, 'final', 0)

__version__ = str(packaging.version.Version('.'.join(str(p) for p in VERSION)))
