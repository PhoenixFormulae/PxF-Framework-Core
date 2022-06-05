## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


# TODO: Decide how to acquire the game phase and its related managers
#       And if the managers should be singletons or not
class ManagerInterface(ABC):
	
	@abstractmethod
	def Ready(self):
		pass

