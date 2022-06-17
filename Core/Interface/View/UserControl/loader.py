## System Imports
from pathlib import Path


## Application Imports
from Core.Interface.View.UserControl.base import BaseUserControl
from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Parsers.Interface.UserControl.Formats.JSON import UserControlData


## Library Imports


class UserControlLoader:
	
	@staticmethod
	def Load(path: str) -> UserControlInterface:
		script_path = Path(path)
		script_json = script_path.read_text()
		
		data = UserControlData.from_json(script_json)
		
		return BaseUserControl(data)
