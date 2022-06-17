## System Imports
from abc import abstractmethod
from typing import Optional, Union, List, TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Core.Interface.View.Event.interfaces import EventInterface

from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Interface.View.Control.metaclasses import ControlMetaInterfaceMixin


## Library Imports


class ControlInterface(metaclass=ControlMetaInterfaceMixin):
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@Name.setter
	@abstractmethod
	def Name(self, value: str) -> str:
		pass
	
	@property
	@abstractmethod
	def Type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Width(self) -> int:
		pass
	
	@property
	@abstractmethod
	def Height(self) -> int:
		pass
	
	@property
	@abstractmethod
	def GlobalPosition(self) -> tuple[int, int]:
		pass
	
	@property
	@abstractmethod
	def RequiredProperties(self) -> list[str]:
		pass
	
	@property
	@abstractmethod
	def OptionalProperties(self) -> list[str]:
		pass
	
	@property
	@abstractmethod
	def Children(self) -> List[ControlMetaInterfaceMixin]:
		pass
	
	@property
	@abstractmethod
	def User_controls(self) -> List:
		pass
	
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def __del__(self):
		pass
	
	############### General Methods ################
	
	@abstractmethod
	def AddChild(self, control: ControlMetaInterfaceMixin):
		pass
	
	@abstractmethod
	def AddChildren(self, controls: List[ControlMetaInterfaceMixin]):
		pass
	
	@abstractmethod
	def FindChild(self, child_name: str) -> Optional[ControlMetaInterfaceMixin]:
		pass
	
	@abstractmethod
	def AddUserControl(self, user_control: Union[UserControlInterface, List[UserControlInterface]]):
		pass
	
	@abstractmethod
	def SetParent(self, parent: ControlMetaInterfaceMixin):
		pass
	
	@abstractmethod
	def AddEvent(self, event: 'EventInterface'):
		pass
	
	@abstractmethod
	def Validated(self):
		pass
	
	@abstractmethod
	def Validate(self):
		pass
	
	@abstractmethod
	def Invalidate(self):
		pass
