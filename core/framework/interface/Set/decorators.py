## framework imports
from typing import Type


## Application imports


## Library imports
from core.framework import FrameInterface
from core.framework import InterfaceSetInterface


def register_interface_set(frame: Type[FrameInterface]):
	
	def decorator(cls: Type[InterfaceSetInterface]):
		
		frame.RegisterInterfaceSet(cls)
		
		return cls
	
	return decorator
