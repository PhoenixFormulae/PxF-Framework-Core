## System Imports
from typing import Type


## Application Imports
from Core.Manager.interfaces import ManagerInterface
from Core.System.interfaces import GameSystemInterface


## Library Imports


def register_manager(system: Type[GameSystemInterface]):
	
	def decorator(manager: Type[ManagerInterface]):
		
		system.RegisterManager(manager)
		
		return manager
	
	return decorator

