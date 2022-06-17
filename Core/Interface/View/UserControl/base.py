## System Imports
from typing import TYPE_CHECKING


## Application Imports


## Library Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.View.Event.loader import EventLoader
from Core.Interface.Frame.interfaces import FrameInterface
from Core.Interface.View.Control.loader import ControlLoader
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Parsers.Interface.UserControl.Formats.JSON import UserControlData


class BaseUserControl(UserControlInterface):
	
	@property
	def Type(self) -> str:
		return self._user_control_properties['name']
	
	@property
	def UserControlProperties(self) -> dict:
		return self._user_control_properties
	
	@property
	def ControlProperties(self) -> dict:
		return self._control_properties
	
	@property
	def EventProperties(self) -> dict:
		return None
	
	def __init__(self, data: UserControlData):
		self._control_properties: dict = {}
		self._user_control_properties: dict = data.to_dict()
	
	def Initialize(self, frame: FrameInterface, view: ViewInterface) -> ControlInterface:
		control_loader: ControlLoader = ControlLoader(frame, None, view)
		
		control: ControlInterface = control_loader.LoadUserControl(self.__data)
		
		return control
