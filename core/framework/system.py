# System imports
import logging
from typing import Type

# Local imports
from core.framework import plugins
from core.framework.system.interfaces import GameSystemInterface
from core.framework.system_manager import SystemManager


# External imports


class CoreSystem:
	
	GameSystemTypes: list[Type[GameSystemInterface]] = []
	GameSystem: GameSystemInterface = None
	BootGameSystem: bool = True
	
	Plugins: None = None
	
	@classmethod
	def register_game_system(cls, game_system_type: Type[GameSystemInterface]):
		if game_system_type not in cls.GameSystemTypes:
			cls.GameSystemTypes.append(game_system_type)
	
	@classmethod
	def initialize(cls):
		logging.debug('Initializing core framework')
	
	@classmethod
	def run(cls):
		cls.Plugins = plugins.Initialize()
		
		if cls.BootGameSystem:
			cls.GameSystem.Ready()
		else:
			SystemManager.Ready()
	
