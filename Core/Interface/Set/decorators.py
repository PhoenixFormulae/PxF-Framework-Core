## System Imports
from typing import Type


## Application Imports


## Library Imports
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.Set.interfaces import InterfaceSetInterface


def register_interface_set(frame: Type[FrameInterface]):
	
	def decorator(cls: Type[InterfaceSetInterface]):
		
		frame.RegisterInterfaceSet(cls)
		
		return cls
	
	return decorator
