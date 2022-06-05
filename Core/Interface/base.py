## System Imports
import logging
from abc import ABC
from typing import Type
from threading import Thread


## Application Imports


## Library Imports
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.interfaces import FrameInterfaceInterface


class BaseFrameInterface(FrameInterfaceInterface, ABC):
	
	@property
	def Frames(self) -> list[FrameInterface]:
		return self._frames
	
	@property
	def Sets(self) -> list[InterfaceSetInterface]:
		return self._sets
	
	def __init__(self):
		self._frames: list[FrameInterface] = []
		self._sets: list[InterfaceSetInterface] = []
	
	def GetFrameInstance(self, frame_type: Type[FrameInterface]) -> FrameInterface | None:
		for frame in self.Frames:
			if type(frame) == frame_type:
				return frame
		
		return None
	
	def Ready(self):
		for set in self.Sets:
			set.Ready()
		
		self._ReadySingular()
	
	def _ReadyThreaded(self):
		logging.debug("Looping interface frames")
		
		for frame in self.Frames:
			frame_thread = Thread(target=frame.Loop, daemon=True)
			frame_thread.start()
	
	def _ReadySingular(self):
		logging.debug("Looping interface frames")
		
		for frame in self.Frames:
			frame.Loop()

