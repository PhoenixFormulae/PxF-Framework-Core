## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.View.Control.container import ControlContainer
from Core.Interface.View.UserControl.container import UserControlContainer


class FrameInterface(ABC):
	
	@property
	@abstractmethod
	def Type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def InterfaceSets(self) -> list[InterfaceSetInterface]:
		pass
	
	@property
	@abstractmethod
	def control_types(self) -> ControlContainer:
		pass
	
	@property
	@abstractmethod
	def user_control_types(self) -> UserControlContainer:
		pass
	
	@property
	@abstractmethod
	def event_types(self):
		pass
	
	@classmethod
	@abstractmethod
	def RegisterInterfaceSet(cls, interface_set: InterfaceSetInterface):
		pass
	
	@abstractmethod
	def Loop(self):
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

