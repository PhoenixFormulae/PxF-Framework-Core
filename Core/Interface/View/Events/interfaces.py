## System Imports
from abc import ABC, abstractmethod
from typing import Callable, List, Dict


## Application Imports
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.Events.metaclasses import EventMetaInterfaceMixin


## Library Imports


class EventArgumentsInterface(ABC):
	
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def __del__(self):
		pass


class EventInterface(metaclass=EventMetaInterfaceMixin):
	
	@property
	@abstractmethod
	def type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def children(self) -> List:
		pass
	
	@property
	@abstractmethod
	def subscribers(self) -> List[Callable]:
		pass
	
	@property
	@abstractmethod
	def properties(self) -> Dict[str, object]:
		pass
	
	@abstractmethod
	def SetProperty(self, name: str, value: object):
		pass
	
	@abstractmethod
	def AddChildren(self, events: List[EventMetaInterfaceMixin]):
		pass
	
	@abstractmethod
	def AddSubscriber(self, subscriber: Callable, recursive: bool):
		pass
	
	@abstractmethod
	def AddControl(self, control: ControlInterface):
		pass
	
	@abstractmethod
	def Bind(self, subscriber: Callable):
		pass
	
	@abstractmethod
	def Trigger(self, arguments: EventArgumentsInterface = None):
		pass
