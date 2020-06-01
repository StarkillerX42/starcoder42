"""This is my own code library. It has many cool functions using the numpy and
sympy libraries. Everything tries to be in snake_case, but dictionary keys are
still in CapitalCase. For more extensions on this involving sympy, try
python.math. It's recommended you import this via
import python as s
import python.math

Notable features:
s.reload: A function to reload packages
s.estimate_rgb: A function to give a color of a spectra
s.find_index: A function that can find the closest corresponding index, even if
    your guess isn't in the array
s.describe: A function to describe the contents of a multidimensional array
"""

__version__ = '3.7.2'
__author__ = "Dylan Gatlin"

import sys

if sys.version_info.major == 3:
    from .funcpy3 import *
    from python.physics import *

from .funcpy import *
from .constants import *
from .conversions import *
from .errors import *
from .plotting import *

