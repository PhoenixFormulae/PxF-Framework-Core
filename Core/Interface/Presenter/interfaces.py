## System Imports
from abc import ABC, abstractmethod
from typing import Type


## Application Imports


## Library Imports
from Core.Interface.View.interfaces import ViewInterface


class PresenterInterface(ABC):
	
	@property
	@abstractmethod
	def ViewTypes(self) -> list[Type[ViewInterface]]:
		pass
	
	@property
	@abstractmethod
	def Views(self) -> list[ViewInterface]:
		pass
	
	@classmethod
	@abstractmethod
	def RegisterView(cls, view: ViewInterface):
		pass
	
	@classmethod
	@abstractmethod
	def Ready(cls):
		pass
	
