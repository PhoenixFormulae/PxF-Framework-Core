## System Imports
from abc import abstractmethod, ABC
from typing import Type, TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Core.Interface.Frame.interfaces import FrameInterface
	from Core.Interface.Presenter.interfaces import PresenterInterface
	from Core.Interface.View.UserControl.container import UserControlContainer


## Library Imports


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
	
	