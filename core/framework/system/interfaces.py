## framework imports
from typing import Type
from abc import ABC, abstractmethod


## Application imports
from core.framework import ManagerInterface
from core.framework import GameSystemConfiguration
from core.framework import FrameInterface
from core.framework import PresenterInterface


## Library imports


class GameSystemInterface(ABC):
	
	@property
	@abstractmethod
	def Configuration(self) -> GameSystemConfiguration:
		pass
	
	@property
	@abstractmethod
	def Frames(self) -> list[Type[FrameInterface]]:
		pass
	
	@property
	@abstractmethod
	def ManagerTypes(self) -> list[Type[ManagerInterface]]:
		pass
	
	@property
	@abstractmethod
	def PresenterTypes(self) -> list[Type[PresenterInterface]]:
		pass
	
	@abstractmethod
	def Ready(self):
		pass
	
	@abstractmethod
	def InitializeInterface(self):
		pass
	
	@classmethod
	@abstractmethod
	def register_manager(cls, manager_type: Type[ManagerInterface]):
		pass
	
	@classmethod
	@abstractmethod
	def register_presenter(cls, presenter_type: Type[PresenterInterface]):
		pass
	
