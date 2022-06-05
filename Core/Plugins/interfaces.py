## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


class PluginInterface(ABC):
	
	@abstractmethod
	def Initialize(self):
		pass
	
	@abstractmethod
	def Ready(self):
		pass
