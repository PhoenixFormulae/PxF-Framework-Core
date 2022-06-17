## System Imports
import logging
from typing import Type


## Application Imports
from Core import Plugins
from Core.system_manager import SystemManager
from Core.System.interfaces import GameSystemInterface


## Library Imports


class CoreSystem:
	
	GameSystemTypes: list[Type[GameSystemInterface]] = []
	GameSystem: GameSystemInterface = None
	BootGameSystem: bool = True
	
	Plugins: None = None
	
	@classmethod
	def RegisterGameSystem(cls, game_system_type: Type[GameSystemInterface]):
		if game_system_type not in cls.GameSystemTypes:
			cls.GameSystemTypes.append(game_system_type)
	
	@classmethod
	def Initialize(cls):
		logging.debug('Initializing core system')
	
	@classmethod
	def Run(cls):
		cls.Plugins = Plugins.Initialize()
		
		if cls.BootGameSystem:
			cls.GameSystem.Ready()
		else:
			SystemManager.Ready()
	
