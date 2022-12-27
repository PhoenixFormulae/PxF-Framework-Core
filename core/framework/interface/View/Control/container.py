## framework imports
from typing import List, Type, Iterable, Iterator, MutableSequence


## Application imports
from core.framework import discovery
from core.framework import FrameInterface
from core.framework import ControlInterface


## Library imports


# TODO: Since these types containers are similar (user_control, Event), perhaps they can be made generic
#       with some abstraction
class ControlContainer(Iterable):
	
	def __init__(self, path: MutableSequence[str]):
		self.__path = path
		self.__control_types: List[type(ControlInterface)] = discovery.get_controls(path)
	
	def __iter__(self) -> Iterator[Type[ControlInterface]]:
		yield self.__control_types
	
	def __len__(self) -> int:
		raise len(self.__control_types)
	
	def __add__(self, control_type: Type[ControlInterface]):
		if control_type not in self.__control_types:
			self.__control_types.append(control_type)
		
		return self
	
	def FindType(self, name: str) -> Type[ControlInterface] | None:
		for control_type in self.__control_types:
			if name.lower() == control_type.Type.lower():
				return control_type
		
		return None
	
	def DiscoverTypes(self, frame: FrameInterface, path: MutableSequence[str]):
		pass
	
	def DiscoverScripts(self, frame: FrameInterface, path: str):
		pass
	