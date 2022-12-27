## framework imports
from typing import Type


## Application imports
from core.framework import CoreSystem


## Library imports
from core.framework import GameSystemInterface


def register_game_system():
	
	def decorator(game_system: Type[GameSystemInterface]):
		CoreSystem.register_game_system(game_system)
		
		return game_system
	
	return decorator
