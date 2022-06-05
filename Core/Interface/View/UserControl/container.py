## System Imports
from typing import List


## Application Imports
from Core.Interface.View.UserControl.interfaces import UserControlInterface


## Library Imports


class UserControlContainer:
	
	def __init__(self):
		self.__user_control_types: List[UserControlInterface] = []
	
	def AddUserControl(self, control: UserControlInterface | type(UserControlInterface)):
		if control not in self.__user_control_types:
			self.__user_control_types.append(control)
	
	def AddUserControls(self, controls: List[UserControlInterface]):
		for control in controls:
			if control not in self.__user_control_types:
				self.__user_control_types.append(control)
	
	def FindUserControl(self, name: str) -> UserControlInterface | None:
		for user_control_type in self.__user_control_types:
			if name.lower() == user_control_type.type.lower():
				return user_control_type
		
		return None

