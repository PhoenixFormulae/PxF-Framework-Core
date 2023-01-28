# Standard Imports
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

# Local Imports
if TYPE_CHECKING:
    from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC

# External Imports


class UserControlABC(ABC):
    @property
    @abstractmethod
    def kind(self) -> str:
        pass

    @property
    @abstractmethod
    def user_control_properties(self) -> dict:
        pass

    @property
    @abstractmethod
    def control_properties(self) -> dict:
        pass

    @property
    @abstractmethod
    def event_properties(self) -> dict:
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init(self, frame, view) -> Optional['ControlABC']:
        pass
