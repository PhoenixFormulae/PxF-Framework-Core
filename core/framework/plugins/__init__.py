## framework imports
import logging


## Application imports


## Library imports
from core.framework import loader
from core.framework import GameSystemInterface


def Initialize():
	logging.info("Loading plugin packages")
	loader.load_all_packages()
	


