## System Imports
from abc import abstractmethod
from typing import Type, TYPE_CHECKING


## Application Imports


## Library Imports
if TYPE_CHECKING:
	from Core.Interface.Frame.interfaces import FrameInterface

from Core.Interface.Presenter.interfaces import PresenterInterface


class InterfaceSetInterface:
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Frame(self) -> 'FrameInterface':
		pass
	
	@property
	@abstractmethod
	def PresenterTypes(self) -> list[Type[PresenterInterface]]:
		pass
	
	@property
	@abstractmethod
	def AssetsDirectory(self) -> str:
		pass
	
	@classmethod
	@abstractmethod
	def RegisterPresenter(cls, presenter: Type[PresenterInterface]):
		pass
	
	def Ready(self):
		pass
	
