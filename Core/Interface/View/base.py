## System Imports
from abc import ABC
from pathlib import Path
from typing import Optional, List


## Application Imports
from System.Interface.View.ViewLoader import ViewLoader


## Library Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.View.Events.container import EventContainer
from Core.Interface.View.Control.interfaces import ControlInterface


class BaseView(ViewInterface, ABC):
	
	@property
	def controls(self) -> List[ControlInterface]:
		return self.__controls
	
	@property
	def events(self) -> EventContainer:
		return self.__event_container
	
	def __init__(self, name: str):
		self.__controls: List[ControlInterface] = []
		self.__event_container = EventContainer()
		
		self.__path = Path(name)
		self.__loaded: bool = False
		
		ViewLoader().Load(self, self.__path.__str__())
		
		self._Prepare()
	
	def _Prepare(self):
		pass
	
	def Show(self):
		# TODO: Showing root level controls should be enough to show the view as it would not be necessary to
		#       alter the final desired state of children visibility
		for control in self.__controls:
			control.Show()
	
	def Hide(self):
		for control in self.__controls:
			control.Hide()
	
	def AddControl(self, control: ControlInterface):
		if control not in self.__controls:
			self.__controls.append(control)
	
	def FindControl(self, control_name: str, recursive: bool = True) -> Optional[ControlInterface]:
		for control in self.__controls:
			control: ControlInterface = control
			
			if control.name == control_name:
				return control
			
			if recursive:
				return control.FindChild(control_name)
		
		return None
	
	def OnPreLoad(self):
		pass
	
	def OnLoad(self):
		if self.__loaded:
			return
		
		for control in self.__controls:
			self.call_child(control, 'OnViewLoad')
		
		self.__loaded = True
	
	def OnPostLoad(self):
		for control in self.__controls:
			self.call_child(control, 'OnViewPostLoad')
	
	@staticmethod
	def call_child(control: ControlInterface, name: str):
		if not hasattr(control, name):
			return
		
		call = getattr(control, name)
		
		if callable(call):
			call()

