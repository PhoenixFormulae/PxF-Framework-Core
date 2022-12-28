# System imports
from abc import ABC, abstractmethod
from typing import Callable, List, Dict

from core.framework.interface.view.control.interfaces import ControlABC
# Local imports
from core.framework.interface.view.event.metaclasses import EventMetaABCMixin


# External imports


class EventArgsABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass


class EventABC(metaclass=EventMetaABCMixin):

    @property
    @abstractmethod
    def kind(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, val: str):
        pass

    @property
    @abstractmethod
    def children(self) -> List:
        pass

    @property
    @abstractmethod
    def subscribers(self) -> List[Callable]:
        pass

    @property
    @abstractmethod
    def properties(self) -> Dict[str, object]:
        pass

    @abstractmethod
    def set_property(self, name: str, value: object):
        pass

    @abstractmethod
    def add_children(self, events: List[EventMetaABCMixin]):
        pass

    @abstractmethod
    def add_subscriber(self, subscriber: Callable, recursive: bool = False):
        pass

    @abstractmethod
    def add_control(self, control: ControlABC):
        pass

    @abstractmethod
    def bind(self, subscriber: Callable):
        pass

    @abstractmethod
    def trigger(self, arguments: EventArgsABC | None = None):
        pass
