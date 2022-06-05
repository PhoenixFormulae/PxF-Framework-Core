## System Imports
import logging
from typing import Type


## Application Imports


## Library Imports
from Core.Systems.interfaces import GameSystemInterface


class CoreSystem:
	
	GameSystemTypes: list[Type[GameSystemInterface]] = []
	GameSystem: GameSystemInterface = None
	BootGameSystem: bool = True
	
	@classmethod
	def Initialize(cls):
		logging.debug('Initializing core system')
	
	@classmethod
	def Run(cls, game_system: GameSystemInterface):
		cls.GameSystem = game_system
		
		if cls.BootGameSystem:
			game_system.Ready()
		else:
			BootSystem.Ready()
	
	@classmethod
	def RegisterGameSystem(cls, game_system_type: Type[GameSystemInterface]):
		if game_system_type not in cls.GameSystemTypes:
			cls.GameSystemTypes.append(game_system_type)
	
	
class BootSystem:
	
	@classmethod
	def Ready(cls):
		pass
	
