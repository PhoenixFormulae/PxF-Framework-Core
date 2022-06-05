## System Imports
from typing import List


## Application Imports
from Core.Interface.View.Events.interfaces import EventInterface


## Library Imports


class EventContainer:
	
	def __init__(self):
		self.__event_types: List[type(EventInterface)] = []
		self.__events: List[EventInterface] = []
	
	def FindEventType(self, name: str) -> EventInterface | None:
		for event_type in self.__event_types:
			if name.lower() == event_type.type.lower():
				return event_type
		
		return None
	
	def AddEvent(self, event: EventInterface):
		if event not in self.__events:
			self.__events.append(event)
	
	def FindEvent(self, event_name: str) -> EventInterface | None:
		for event in self.__events:
			if event.name == event_name:
				return event
		
		return None

