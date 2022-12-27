# framework imports

# Library imports
from core.framework import heuristics, logging


# External imports


def init():
	# sys.path.append(application.GetSuperPath()) # TODO: This needs to be moved elsewhere
	
	logging.Initialize()
	heuristics.init()
	
	CoreSystem.initialize()

