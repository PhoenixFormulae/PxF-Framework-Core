# Standard imports

# Local imports

# External imports
from pxf_framework_core.framework.heuristics import Malloc, Memtrack


def init():
    Malloc.init()
    Memtrack.init()
