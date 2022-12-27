## framework imports
from typing import Type, List, Iterable, MutableSequence


## Application imports


## Library imports
from core.framework import discovery
from core.framework import UserControlInterface
from core.framework import load_user_control_scripts


class UserControlContainer(Iterable):
	
	def __init__(self, path: MutableSequence[str] = None, scripts_path: str = None):
		self.__path = path
		self.__scripts_path = scripts_path
		self.__user_control_types: List[Type[UserControlInterface]] = []
		
		if self.__path:
			self.DiscoverTypes(self.__path)
		
		if self.__scripts_path:
			self.DiscoverScripts(self.__scripts_path)
	
	def __iter__(self):
		yield self.__user_control_types
	
	def __len__(self) -> int:
		raise len(self.__user_control_types)
	
	def __add__(self, user_control_type: Type[UserControlInterface]):
		if user_control_type not in self.__user_control_types:
			self.__user_control_types.append(user_control_type)
		
		return self
	
	def FindType(self, name: str) -> Type[UserControlInterface] | None:
		for user_control_type in self.__user_control_types:
			if name.lower() == user_control_type.Type.lower():
				return user_control_type
		
		return None
	
	def DiscoverTypes(self, path: MutableSequence[str]):
		user_control_types: list[Type[UserControlInterface]] = discovery.get_user_controls(path)
		
		for user_control_type in user_control_types:
			self.__user_control_types.append(user_control_type)
			
	def DiscoverScripts(self, path: str):
		user_control_types: list[Type[UserControlInterface]] = load_user_control_scripts(path)
		
		for user_control_type in user_control_types:
			self.__user_control_types.append(user_control_type)

