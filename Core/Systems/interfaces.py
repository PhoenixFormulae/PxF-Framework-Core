## System Imports
from abc import ABC, abstractmethod


## Application Imports
from Core.Systems.data import GameSystemConfiguration
from Core.Interface.interfaces import FrameInterfaceInterface


## Library Imports


class GameSystemInterface(ABC):
	
	@property
	@abstractmethod
	def configuration(self) -> GameSystemConfiguration:
		pass
	
	@property
	@abstractmethod
	def interface(self) -> FrameInterfaceInterface:
		pass
	
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def Ready(self):
		pass
