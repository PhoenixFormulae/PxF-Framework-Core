## framework imports
from abc import abstractmethod, ABC
from typing import Type, TYPE_CHECKING


## Application imports
if TYPE_CHECKING:
	from core.framework import FrameInterface
	from core.framework import PresenterInterface
	from core.framework import UserControlContainer


## Library imports


class InterfaceSetInterface(ABC):
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def FrameType(self) -> Type['FrameInterface']:
		pass
	
	@property
	@abstractmethod
	def AssetsDirectory(self) -> str:
		pass
	
	@property
	@abstractmethod
	def UserControlTypes(self) -> 'UserControlContainer':
		pass
	
	@classmethod
	@abstractmethod
	def Initialize(cls):
		pass
	
	@classmethod
	@abstractmethod
	def Ready(cls):
		pass
	
	