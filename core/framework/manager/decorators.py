# System imports
from typing import Type

# Local imports
from core.framework.manager.interfaces import ManagerInterface
from core.framework.system.interfaces import GameSystemInterface

# External imports


def register_manager(system: Type[GameSystemInterface]):
	def decorator(manager: Type[ManagerInterface]):
		system.register_manager(manager)

		return manager
	
	return decorator

