## System Imports


## Application Imports
from Core.Heuristics import Malloc, Memtrack, TypeCheck


## Library Imports


def Initialize():
	Malloc.Initialize()
	Memtrack.Initialize()
	TypeCheck.Initialize()
