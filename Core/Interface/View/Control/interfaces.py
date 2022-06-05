## System Imports
from abc import abstractmethod
from typing import Optional, Union, List, TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Core.Interface.View.Events.interfaces import EventInterface

from Core.Interface.View.UserControl.interfaces import UserControlInterface
from Core.Interface.View.Control.metaclasses import ControlMetaInterfaceMixin


## Library Imports


class ControlInterface(metaclass=ControlMetaInterfaceMixin):
	
	@property
	@abstractmethod
	def name(self) -> str:
		pass
	
	@name.setter
	@abstractmethod
	def name(self, value: str) -> str:
		pass
	
	@property
	@abstractmethod
	def type(self) -> str:
		pass
	
	@property
	@abstractmethod
	def children(self) -> List[ControlMetaInterfaceMixin]:
		pass
	
	@property
	@abstractmethod
	def user_controls(self) -> List:
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
