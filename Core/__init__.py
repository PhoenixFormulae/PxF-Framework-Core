## System Imports

## Application Imports
from Core.system import CoreSystem
from Core import Heuristics, Logging


## Library Imports


def Initialize():
	Logging.Initialize()
	Heuristics.Initialize()
	
	CoreSystem.Initialize()

