## System Imports
from typing import Type


## Application Imports
from Core import CoreSystem


## Library Imports
from Core.Systems.interfaces import GameSystemInterface


def register_game_system():
	
	def decorator(game_system: Type[GameSystemInterface]):
		CoreSystem.RegisterGameSystem(game_system)
		
		return game_system
	
	return decorator
