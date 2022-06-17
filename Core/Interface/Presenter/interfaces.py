## System Imports
from typing import List
from abc import ABC, abstractmethod


## Application Imports
from Core.Interface.View.interfaces import ViewInterface


## Library Imports


class PresenterInterface(ABC):
	
	@property
	@abstractmethod
	def ViewTypes(self) -> List[type(ViewInterface)]:
		pass
	
	@property
	@abstractmethod
	def Views(self) -> List[ViewInterface]:
		pass
	
	@classmethod
	@abstractmethod
	def RegisterView(cls, view: ViewInterface):
		pass
	
	@classmethod
	@abstractmethod
	def Ready(cls):
		pass
	
