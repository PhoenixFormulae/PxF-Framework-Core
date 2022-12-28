# Standard imports

# Local imports
from core.framework.heuristics import Malloc, Memtrack


# External imports


def init():
    Malloc.init()
    Memtrack.init()
