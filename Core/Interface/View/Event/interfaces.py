## System Imports
from abc import ABC, abstractmethod
from typing import Callable, List, Dict


## Application Imports
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.Event.metaclasses import EventMetaInterfaceMixin


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
	def Type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Children(self) -> List:
		pass
	
	@property
	@abstractmethod
	def Subscribers(self) -> List[Callable]:
		pass
	
	@property
	@abstractmethod
	def Properties(self) -> Dict[str, object]:
		pass
	
	@abstractmethod
	def SetProperty(self, name: str, value: object):
		pass
	
	@abstractmethod
	def AddChildren(self, events: List[EventMetaInterfaceMixin]):
		pass
	
	@abstractmethod
	def AddSubscriber(self, subscriber: Callable, recursive: bool = False):
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
