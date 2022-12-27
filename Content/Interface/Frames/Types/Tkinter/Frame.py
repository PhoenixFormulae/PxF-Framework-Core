## framework imports
from typing import List, Type

## Application imports
from core.framework import BaseFrame
from core.framework import discovery
from core.framework import BaseWindowConfiguration
from core.framework import ViewInterface
from core.framework import FrameWindowInterface
from core.framework import ControlInterface
from core.framework import UserControlInterface

## Library imports
from Content.Interface.Types.Tkinter import Controls
from Content.Interface.Frames.Types.Tkinter.Window import TkinterWindow


class TkinterFrame(BaseFrame):
	
	Type: str = "Tkinter"
	SingleWindow: bool = False
	
	@property
	def views(self) -> List[ViewInterface]:
		return self.__views
	
	@property
	def windows(self) -> List[FrameWindowInterface]:
		return self.__windows
	
	@property
	def control_types(self) -> List[ControlInterface]:
		return self.__controls
	
	@property
	def user_control_types(self) -> List[UserControlInterface]:
		return self.__user_controls
	
	@property
	def window_type(self) -> type(FrameWindowInterface):
		return self.__window_type
	
	def __init__(self):
		super().__init__()
		
		self.__views: List[ViewInterface] = []
		self.__window_configuration = BaseWindowConfiguration()
		self.__windows: List[TkinterWindow] = []
		
		self.__controls: List[ControlInterface] = []
		self.__user_controls: List[UserControlInterface] = []
		
		self.__window_type: Type[FrameWindowInterface] = TkinterWindow
	
	def Initialize(self):
		self.__controls = discovery.get_controls(Controls.__path__)
		self.__windows.append(TkinterWindow(self, self.__window_configuration))
	
	def Loop(self):
		if len(self.__windows) > 0:
			self.__windows[0].Loop()
