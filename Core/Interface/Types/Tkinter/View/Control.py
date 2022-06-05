## System Imports
from typing import List, Union, Optional
from tkinter import ttk


## Application Imports
from Core.Interface.View.Events.interfaces import EventInterface
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Interface.View.Control.metaclasses import ControlMetaInterfaceMixin


## Library Imports


class Control(ControlInterface, ttk.Widget):
	
	type: str = "control"
	
	@property
	def name(self) -> str:
		return self.__name
	
	@property
	def children(self) -> List[ControlInterface]:
		return self.__children
	
	@property
	def user_controls(self) -> List:
		return self.__user_controls
	
	def __init__(self):
		super().__init__()
		
		self.__name = ''
		self.__children = []
		
		self.__controls = []
		self.__user_controls = []
	
	def __del__(self):
		super(ttk.Widget, self).destroy()
	
	def AddChild(self, control: ControlMetaInterfaceMixin):
		pass
	
	def AddChildren(self, controls: List[ControlMetaInterfaceMixin]):
		pass
	
	def FindChild(self, child_name: str) -> Optional[ControlMetaInterfaceMixin]:
		pass
	
	def AddUserControl(self, user_control: Union[UserControlInterface, List[UserControlInterface]]):
		pass
	
	def SetParent(self, parent: ControlMetaInterfaceMixin):
		pass
	
	def AddEvent(self, event: EventInterface):
		pass
	
	def Validated(self):
		pass
	
	def Validate(self):
		pass
	
	def Invalidate(self):
		pass
