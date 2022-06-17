## System Imports
import logging


## Application Imports


## Library Imports
from Core.Plugins import loader
from Core.System.interfaces import GameSystemInterface


def Initialize():
	logging.info("Loading plugin packages")
	loader.load_all_packages()
	


