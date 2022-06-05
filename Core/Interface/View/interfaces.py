## System Imports
from typing import Optional, List
from abc import ABC, abstractmethod


## Application Imports
from Core.Interface.View.Events.container import EventContainer
from Core.Interface.View.Control.interfaces import ControlInterface


## Library Imports

class ViewInterface(ABC):
	
	@property
	@abstractmethod
	def controls(self) -> List[ControlInterface]:
		pass
	
	@property
	@abstractmethod
	def events(self) -> EventContainer:
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
	
