## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


class ManagerInterface(ABC):
	
	@classmethod
	@abstractmethod
	def Ready(cls):
		pass

