## System Imports
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Core.Interface.View.Control.interfaces import ControlInterface


## Library Imports


class UserControlInterface(ABC):
	
	@property
	@abstractmethod
	def Type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def UserControlProperties(self) -> dict:
		pass
	
	@property
	@abstractmethod
	def ControlProperties(self) -> dict:
		pass
	
	@property
	@abstractmethod
	def EventProperties(self) -> dict:
		pass
	
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def Initialize(self, frame, view) -> Optional['ControlInterface']:
		pass
