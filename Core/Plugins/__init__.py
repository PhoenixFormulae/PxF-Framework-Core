## System Imports
import logging


## Application Imports


## Library Imports
from Core.Plugins import loader
from Core.Systems.interfaces import GameSystemInterface


def Initialize(system: GameSystemInterface):
	logging.info("Loading plugin packages")
	loader.load_all_packages(system)
	


