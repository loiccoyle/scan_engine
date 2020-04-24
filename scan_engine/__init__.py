'''scan_engine allows for full control over parameter scans.

Classes:
    Productable: handles the parameters which should obey the cartesian
    product rule.

    Zipable: handles the parameters which should obey the simultaneous
    iteration, i.e. zip.

    combine: a function to expand nested combinations.
'''
from .combinations import Productable, Zipable
from .combine import combine

__all__ = ['Productable', 'Zipable', 'combine']
__author__ = 'Loic Coyle <loic.coyle@hotmail.fr>'
__version__ = '0.1.0'
