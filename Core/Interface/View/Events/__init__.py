## System Imports
from typing import Callable, List, Dict, Any, Optional


## Application Imports
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.Events.interfaces import EventInterface, EventArgumentsInterface


# Library Imports


class Event(EventInterface):
	"""
	An event is an action that can be registered to occur when
	other action occurs, for example when the user clicks
	a button in the mouse the registered methods will be called.
	"""
	
	type: str = "event"
	
	@property
	def name(self) -> str | None:
		return self.__properties.get('name')
	
	@property
	def children(self) -> List[EventInterface]:
		return self.__children
	
	@property
	def controls(self) -> List[ControlInterface]:
		return self.__controls
	
	@property
	def subscribers(self) -> List[Callable]:
		return self.__subscribers
	
	@property
	def properties(self) -> Dict[str, Any]:
		return self.__properties
	
	def __init__(self):
		self.__parent: Optional[EventInterface] = None
		
		self.__children: List[EventInterface] = []
		self.__controls: List[ControlInterface] = []
		self.__subscribers: List[Callable] = []
		self.__properties: Dict[str, Any] = {}
	
	def SetProperty(self, name: str, value: object):
		## TODO: Do proper check and resolution of value types
		self.__properties[name] = value
	
	def AddChildren(self, events: List):
		for event in events:
			if event not in self.children:
				self.children.append(event)
				event.SetParent(self)
	
	def SetParent(self, parent: EventInterface):
		self.__parent = parent
	
	def AddSubscriber(self, subscriber: Callable, recursive: bool = False):
		if subscriber not in self.__subscribers:
			self.__subscribers.append(subscriber)
		
		if recursive:
			for event in self.__children:
				event.AddSubscriber(subscriber, True)
	
	def AddControl(self, control: ControlInterface):
		if control not in self.__controls:
			self.__controls.append(control)
	
	def Bind(self, subscriber: Callable):
		if subscriber not in self.__subscribers:
			self.__subscribers.append(subscriber)
	
	def Trigger(self, args: EventArgumentsInterface = None):
		for subscriber in self.__subscribers:
			if args:
				subscriber(args)
			else:
				subscriber()
