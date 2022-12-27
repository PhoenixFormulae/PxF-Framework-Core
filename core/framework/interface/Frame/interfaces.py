## framework imports
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod


## Application imports
from core.framework import InterfaceSetInterface
from core.framework import ControlInterface

if TYPE_CHECKING:
	from core.framework import ControlContainer
	from core.framework import UserControlContainer


## Library imports


class FrameInterface(ABC):
	
	@property
	@abstractmethod
	def Type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def AssetsDirectory(self) -> str:
		pass
	
	@property
	@abstractmethod
	def InterfaceSets(self) -> list[type(InterfaceSetInterface)]:
		pass
	
	@property
	@abstractmethod
	def BaseControlType(self) -> type(ControlInterface):
		pass
	
	@property
	@abstractmethod
	def ControlTypes(self) -> 'ControlContainer':
		pass
	
	@property
	@abstractmethod
	def UserControlTypes(self) -> 'UserControlContainer':
		pass
	
	@property
	@abstractmethod
	def EventTypes(self):
		pass
	
	@classmethod
	@abstractmethod
	def RegisterInterfaceSet(cls, interface_set: type(InterfaceSetInterface)):
		pass
	
	@classmethod
	@abstractmethod
	def Initialize(cls):
		pass
	
	@classmethod
	@abstractmethod
	def Ready(cls):
		pass
	
	@classmethod
	@abstractmethod
	def Loop(cls):
		pass


class FrameWindowInterface(ABC):
	
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def __del__(self):
		pass
	
	@abstractmethod
	def Loop(self):
		pass

