## System Imports
from typing import Type


## Application Imports


## Library Imports
from Core.System.interfaces import GameSystemInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


def register_presenter(game_system: Type[GameSystemInterface]):

	def decorator(cls: Type[PresenterInterface]):
		
		game_system.RegisterPresenter(cls)
		
		return cls
	
	return decorator

