## framework imports
from abc import ABC
from pathlib import Path
from typing import Optional, List


## Application imports
from core.framework import ViewLoader
from core.framework import ViewInterface
from core.framework import EventContainer
from core.framework import EventInterface
from core.framework import PropertiesEventDispatcher
from core.framework import ControlInterface


## Library imports


class BaseView(ViewInterface, ABC):
	
	@property
	def Controls(self) -> List[ControlInterface]:
		return self.__controls
	
	@property
	def Events(self) -> EventContainer:
		return self.__event_container
	
	def __init__(self):
		super().__init__()
		
		self.__controls: List[ControlInterface] = []
		self.__events: List[EventInterface] = []
		
		self.__event_container = None  # EventContainer()
		
		self.__path: str | None = None
		self.__loaded: bool = False
		
		self.__view_loader = ViewLoader(self, self.FrameType, self.InterfaceSetType)
	
	def Ready(self):
		pass
	
	def _Prepare(self):
		pass
	
	def _Load(self, path: str):
		if self.__loaded:
			raise Exception('view was already loaded, cannot load again')
		
		self.__path = Path(path)
		
		self.__view_loader.Load(self.__path.__str__())
		self.__loaded = True
		
		self.Hide()
	
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
			
			if control.Name == control_name:
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

