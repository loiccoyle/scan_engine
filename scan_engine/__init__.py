'''scan_engine allows for full control over parameter scans.

Classes:
    Productable: handles the parameters which should obey the cartesian
    product rule.

    Zipable: handles the parameters which should obey the simultaneous
    iteration, i.e. zip.

    engine: a function to expand nested operations.
'''

from pkg_resources import get_distribution, DistributionNotFound

from .parameters import Productable, Zipable
from .engine import engine

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = 'unkown'

__all__ = ['Productable', 'Zipable', 'engine']
