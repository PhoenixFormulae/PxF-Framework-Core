## System Imports
from typing import List
from abc import ABC, abstractmethod


## Application Imports


## Library Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Frame.interfaces import FrameInterface


class FrameInterfaceInterface(ABC):
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Frames(self) -> List[FrameInterface]:
		pass
	
	@abstractmethod
	def GetFrameInstance(self, frame_type: type(FrameInterface)) -> ViewInterface:
		pass
	
	@abstractmethod
	def Ready(self):
		pass

