## System Imports
import sys
from junctions import application


## Application Imports
from Core.system import CoreSystem
from Core import Heuristics, Logging


## Library Imports


def Initialize():
	# sys.path.append(app.GetSuperPath()) # TODO: This needs to be moved elsewhere
	
	Logging.Initialize()
	Heuristics.Initialize()
	
	CoreSystem.Initialize()

