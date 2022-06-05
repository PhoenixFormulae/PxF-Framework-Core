## System Imports
from typing import List


## Application Imports
from Core.Interface.View.Control.interfaces import ControlInterface


## Library Imports


# TODO: Since these types containers are similar (UserControl, Event), perhaps they can be made generic for abstraction
class ControlContainer:
	
	def __init__(self):
		self.__control_types: List[type(ControlInterface)] = []
		
	def AddControl(self, control: type(ControlInterface) | ControlInterface):
		if isinstance(control, list):
			for ctrl in control:
				if ctrl not in self.__control_types:
					self.__control_types.append(ctrl)
		
		elif issubclass(control, ControlInterface):
			if control not in self.__control_types:
				self.__control_types.append(control)
	
	def AddControls(self, controls: List[ControlInterface]):
		for control in controls:
			if control not in self.__control_types:
				self.__control_types.append(control)
	
	def FindControlType(self, name: str) -> type(ControlInterface) | None:
		for control_type in self.__control_types:
			if name.lower() == control_type.type.lower():
				return control_type
		
		return None
