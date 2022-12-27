## framework imports
from typing import Optional, List, Type
from abc import ABC, abstractmethod


## Application imports
from core.framework import FrameInterface
from core.framework import EventContainer
from core.framework import InterfaceSetInterface
from core.framework import PropertiesEventDispatcher
from core.framework import ControlInterface


## Library imports


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
	
