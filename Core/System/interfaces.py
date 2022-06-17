## System Imports
from typing import Type
from abc import ABC, abstractmethod


## Application Imports
from Core.Manager.interfaces import ManagerInterface
from Core.System.data import GameSystemConfiguration
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


## Library Imports


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
	def RegisterManager(cls, manager_type: Type[ManagerInterface]):
		pass
	
	@classmethod
	@abstractmethod
	def RegisterPresenter(cls, presenter_type: Type[PresenterInterface]):
		pass
	
