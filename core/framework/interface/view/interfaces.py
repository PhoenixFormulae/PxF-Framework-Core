# System imports
from typing import Optional, List, Type
from abc import ABC, abstractmethod

# Local imports
from core.framework.interface.frame.interfaces import FrameABC
from core.framework.interface.set.interfaces import InterfaceSetABC
from core.framework.interface.view.control.interfaces import ControlABC
from core.framework.interface.view.event.container import EventContainer
from core.framework.properties.dispatcher import PropertiesEventDispatcher


# External imports


class ViewABC(PropertiesEventDispatcher, ABC):

    @property
    @abstractmethod
    def frame_type(self) -> Type[FrameABC]:
        pass

    @property
    @abstractmethod
    def interface_set_type(self) -> Type[InterfaceSetABC]:
        pass

    @property
    @abstractmethod
    def controls(self) -> List[ControlABC]:
        pass

    @property
    @abstractmethod
    def events(self) -> EventContainer:
        pass

    @abstractmethod
    def ready(self):
        pass

    @abstractmethod
    def _prepare(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def add_control(self, control: ControlABC):
        pass

    @abstractmethod
    def find_control(self, control_name: str, recursive: bool = True) -> Optional[ControlABC]:
        pass
