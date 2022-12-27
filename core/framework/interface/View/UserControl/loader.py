## framework imports
from pathlib import Path


## Application imports
from core.framework import BaseUserControl
from core.framework import UserControlInterface
from core.framework import UserControlData


## Library imports


class UserControlLoader:
	
	@staticmethod
	def Load(path: str) -> UserControlInterface:
		script_path = Path(path)
		script_json = script_path.read_text()
		
		data = UserControlData.from_json(script_json)
		
		return BaseUserControl(data)
