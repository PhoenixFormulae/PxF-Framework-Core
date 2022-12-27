## framework imports
from typing import TYPE_CHECKING


## Application imports


## Library imports
from core.framework import ViewInterface
from core.framework import EventLoader
from core.framework import FrameInterface
from core.framework import ControlLoader
from core.framework import ControlInterface
from core.framework import UserControlInterface
from core.framework import UserControlData


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
