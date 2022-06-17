## System Imports


## Application imports
from System.Manager.base import BaseManager


## Library Imports


class SystemManager(BaseManager):
	
	@classmethod
	def Ready(cls):
		from Core.system import CoreSystem
		CoreSystem.GameSystem.InitializeInterface()
		
