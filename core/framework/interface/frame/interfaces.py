# System imports
from typing import TYPE_CHECKING, Type
from abc import ABC, abstractmethod

# Local imports
from core.framework.interface.set.interfaces import InterfaceSetABC
from core.framework.interface.view.control.interfaces import ControlABC

if TYPE_CHECKING:
    from core.framework.interface.view.user_control.container import UserControlContainer
    from core.framework.interface.view.control.container import ControlContainer


# External imports


class FrameABC(ABC):

    @property
    @abstractmethod
    def kind(self) -> str:
        pass

    @property
    @abstractmethod
    def static_window(self) -> bool:
        pass

    @property
    @abstractmethod
    def assets_dir(self) -> str:
        pass

    @property
    @abstractmethod
    def interface_sets(self) -> list[InterfaceSetABC]:
        pass

    @property
    @abstractmethod
    def base_control_type(self) -> Type[ControlABC]:
        pass

    @property
    @abstractmethod
    def control_types(self) -> 'ControlContainer':
        pass

    @property
    @abstractmethod
    def user_control_types(self) -> 'UserControlContainer':
        pass

    @property
    @abstractmethod
    def event_types(self):
        pass

    @classmethod
    @abstractmethod
    def register_interface_set(cls, interface_set: Type[InterfaceSetABC]):
        pass

    @classmethod
    @abstractmethod
    def init(cls):
        pass

    @classmethod
    @abstractmethod
    def ready(cls):
        pass

    @classmethod
    @abstractmethod
    def loop(cls):
        pass


class FrameWindowInterface(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def loop(self):
        pass
