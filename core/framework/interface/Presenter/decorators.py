## framework imports
from typing import Type


## Application imports


## Library imports
from core.framework import GameSystemInterface
from core.framework import PresenterInterface


def register_presenter(game_system: Type[GameSystemInterface]):

	def decorator(cls: Type[PresenterInterface]):
		
		game_system.register_presenter(cls)
		
		return cls
	
	return decorator

