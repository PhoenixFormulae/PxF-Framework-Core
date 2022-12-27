## framework imports
import logging
from abc import ABC
from typing import List
from threading import Thread


## Application imports
from core.framework import ViewInterface
from core.framework import FrameInterface
from core.framework import InterfaceSetInterface


## Library imports


class BaseFrame(FrameInterface, ABC):
	
	InterfaceSets: list[InterfaceSetInterface] = []
	
	@classmethod
	def RegisterInterfaceSet(cls, interface_set: InterfaceSetInterface):
		if interface_set not in cls.InterfaceSets:
			cls.InterfaceSets.append(interface_set)
	
	@classmethod
	def Initialize(cls):
		for interface_set in cls.InterfaceSets:
			interface_set.init()
	
	@classmethod
	def Ready(cls):
		for interface_set in cls.InterfaceSets:
			interface_set.ready()
		
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



