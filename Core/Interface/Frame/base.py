## System Imports
import logging
from abc import ABC
from typing import List
from threading import Thread


## Application Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.Set.interfaces import InterfaceSetInterface


## Library Imports


class BaseFrame(FrameInterface, ABC):
	
	InterfaceSets: list[InterfaceSetInterface] = []
	
	@classmethod
	def RegisterInterfaceSet(cls, interface_set: InterfaceSetInterface):
		if interface_set not in cls.InterfaceSets:
			cls.InterfaceSets.append(interface_set)
	
	@classmethod
	def Initialize(cls):
		for interface_set in cls.InterfaceSets:
			interface_set.Initialize()
	
	@classmethod
	def Ready(cls):
		for interface_set in cls.InterfaceSets:
			interface_set.Ready()
		
		cls._ReadySingular()
	
	@classmethod
	def _ReadyThreaded(cls):
		logging.debug("Looping interface frame in a dedicated thread")
		
		frame_thread = Thread(name=f'{cls.Type} Frame Thread', target=cls.Loop, daemon=True)
		frame_thread.start()
	
	@classmethod
	def _ReadySingular(cls):
		logging.debug("Looping interface frame")
		
		cls.Loop()



