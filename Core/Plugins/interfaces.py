## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


class PluginInterface(ABC):
	
	@property
	@abstractmethod
	def FramesPath(self) -> str:
		pass
	
	@abstractmethod
	def Initialize(self):
		pass
	
	@abstractmethod
	def Ready(self):
		pass
