# Standard imports


# Local imports
from . import logging
from . import heuristics
from .system.core import CoreSystem


# External imports


def init():
    # sys.path.append(application.GetSuperPath()) # TODO: This needs to be moved elsewhere

    logging.Initialize()
    heuristics.init()

    CoreSystem.initialize()
