# System imports
from abc import abstractmethod
from typing import Optional, Union, List, TYPE_CHECKING

# Local imports
from pxf_framework_core.framework.interface.view.control.metaclasses import ControlMetaABCMixin
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC

if TYPE_CHECKING:
    from pxf_framework_core.framework.interface.view.event.interfaces import EventABC

# External imports


class ControlABC(metaclass=ControlMetaABCMixin):  # type: ignore

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
    def kind(self) -> str:
        pass

    @kind.setter
    def kind(self, value):
        pass

    @property
    @abstractmethod
    def width(self) -> int:
        pass

    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def global_position(self) -> tuple[int, int]:
        pass

    @property
    @abstractmethod
    def required_properties(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def optional_properties(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def children(self) -> List['ControlABC']:
        pass

    @property
    @abstractmethod
    def user_controls(self) -> List:
        pass

    @property
    @abstractmethod
    def parent_cls(self) -> 'ControlABC':
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    # General Methods

    @abstractmethod
    def add_child(self, control: 'ControlABC'):
        pass

    @abstractmethod
    def add_children(self, controls: List['ControlABC']):
        pass

    @abstractmethod
    def find_child(self, child_name: str) -> Optional['ControlABC']:
        pass

    @abstractmethod
    def add_user_control(self, user_control: Union[UserControlABC, List[UserControlABC]]):
        pass

    @abstractmethod
    def set_parent(self, parent: 'ControlABC'):
        pass

    @abstractmethod
    def add_event(self, event: 'EventABC'):
        pass

    @abstractmethod
    def validated(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def invalidate(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass
