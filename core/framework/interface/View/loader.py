## framework imports
from pathlib import Path


## Application imports


## Library imports
from core.framework import ViewInterface
from core.framework import FrameInterface
from core.framework import ControlLoader
from core.framework import ViewData
from core.framework import InterfaceSetInterface


class ViewLoader:
	
	def __init__(self, view: ViewInterface, frame: type(FrameInterface), interface_set: type(InterfaceSetInterface)):
		self.__view = view
		self.__frame = frame
		self.__interface_set = interface_set
		
		self.__control_loader = ControlLoader(self.__frame, self.__interface_set, view)
		self.__indent = 1
	
	def Load(self, path: str) -> ViewInterface:
		script_path = Path(path)
		script_json = script_path.read_text()
		view_data = ViewData.from_json(script_json)
		
		self.__LoadScript(view_data)
		
		return self.__view
	
	def __LoadScript(self, data: ViewData):
		view_root = self.__frame.BaseControlType()
		
		self.__control_loader.LoadControlProperties(view_root, data.to_dict())
		
		self.__view.AddControl(view_root)
