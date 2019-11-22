'''scan_engine allows for full control over parameter scans.

Classes:
    Productable: handles the parameters which should obey the cartesian
    product rule.

    Zipable: handles the parameters which should obey the simultaneous
    iteration, i.e. zip.

    engine: a function to expand nested operations.
'''
try:
    from pkg_resources import get_distribution, DistributionNotFound
    __version__ = get_distribution(__name__).version
except (ImportError, DistributionNotFound):
    __version__ = 'unknown'

from .parameters import Productable, Zipable
from .engine import engine

__all__ = ['Productable', 'Zipable', 'engine']
