## System Imports
from typing import Optional, List, Type
from abc import ABC, abstractmethod


## Application Imports
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.View.Event.container import EventContainer
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Properties.dispatcher import PropertiesEventDispatcher
from Core.Interface.View.Control.interfaces import ControlInterface


## Library Imports


class ViewInterface(PropertiesEventDispatcher, ABC):
	
	@property
	@abstractmethod
	def FrameType(self) -> Type[FrameInterface]:
		pass
	
	@property
	@abstractmethod
	def InterfaceSetType(self) -> Type[InterfaceSetInterface]:
		pass
	
	@property
	@abstractmethod
	def Controls(self) -> List[ControlInterface]:
		pass
	
	@property
	@abstractmethod
	def Events(self) -> EventContainer:
		pass
	
	@abstractmethod
	def Ready(self):
		pass
	
	@abstractmethod
	def _Prepare(self):
		pass
	
	@abstractmethod
	def Show(self):
		pass
	
	@abstractmethod
	def Hide(self):
		pass
	
	@abstractmethod
	def AddControl(self, control: ControlInterface):
		pass
	
	@abstractmethod
	def FindControl(self, control_name: str, recursive: bool = True) -> Optional[ControlInterface]:
		pass
	
