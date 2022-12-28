# framework imports

# Library imports
from core.framework import heuristics, logging
from core.framework.system.core import CoreSystem


# External imports


def init():
    # sys.path.append(application.GetSuperPath()) # TODO: This needs to be moved elsewhere

    logging.Initialize()
    heuristics.init()

    CoreSystem.initialize()
