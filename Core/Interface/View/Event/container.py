## System Imports
from typing import List, Iterable, Type, MutableSequence


## Application Imports
from Core.Interface.View.Event import discovery
from Core.Interface.View.Event.interfaces import EventInterface


## Library Imports


class EventContainer(Iterable):
	
	def __init__(self, path: MutableSequence[str]):
		self.__event_types: List[type(EventInterface)] = discovery.get_events(path)
		self.__events: List[EventInterface] = []
	
	def __iter__(self):
		yield self.__event_types
	
	def __add__(self, event_type: Type[EventInterface]):
		if event_type not in self.__event_types:
			self.__event_types.append(event_type)
	
	def __len__(self):
		return len(self.__event_types)
	
	def FindEventType(self, name: str) -> EventInterface | None:
		for event_type in self.__event_types:
			if name.lower() == event_type.type.lower():
				return event_type
		
		return None
	
	def FindEvent(self, event_name: str) -> EventInterface | None:
		for event in self.__events:
			if event.name == event_name:
				return event
		
		return None

