# from . import __version__
from .parameters import Productable, Zipable
from .engine import engine
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

# __verion__ = __version__.version
__all__ = ['Productable', 'Zipable', 'engine']
