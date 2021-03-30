from pkg_resources import packaging

from .constants import DEFAULT_PROTOCOL

__all__ = 'VERSION', '__version__', 'DEFAULT_PROTOCOL'

VERSION = (3, 0, 2, 'dev', 1)

__version__ = str(packaging.version.Version('.'.join(str(p) for p in VERSION)))
