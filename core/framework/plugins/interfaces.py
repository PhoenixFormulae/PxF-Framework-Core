## framework imports
from abc import ABC, abstractmethod


## Application imports


## Library imports


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
