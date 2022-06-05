## System Imports
from abc import ABC
from typing import List


## Application Imports
from Core.Interface.interfaces import FrameInterface
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.View.Events.container import EventContainer
from Core.Interface.View.Control.container import ControlContainer
from Core.Interface.View.UserControl.container import UserControlContainer


## Library Imports


class FrameBase(FrameInterface, ABC):
	
	InterfaceSets: list[InterfaceSetInterface] = []
	
	@property
	def control_types(self) -> ControlContainer:
		return self.__control_types_container
	
	@property
	def user_control_types(self) -> UserControlContainer:
		return self.__user_control_container
	
	@property
	def event_types(self) -> EventContainer:
		return self.__event_types_container
	
	def __init__(self):
		self.__views: List[ViewInterface] = []
		
		self.__control_types_container = ControlContainer()
		self.__user_control_container = UserControlContainer()
		self.__event_types_container = EventContainer()
	
	@classmethod
	def RegisterInterfaceSet(cls, interface_set: InterfaceSetInterface):
		if interface_set not in cls.InterfaceSets:
			cls.InterfaceSets.append(interface_set)
	
	@classmethod
	def Ready(cls):
		pass

