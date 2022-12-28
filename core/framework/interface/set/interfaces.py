# Standard Imports
from abc import abstractmethod, ABC
from typing import Type, TYPE_CHECKING

# Local Imports
if TYPE_CHECKING:
    from core.framework.interface.frame.interfaces import FrameABC
    from core.framework.interface.view.user_control.container import UserControlContainer


# External Imports


class InterfaceSetABC(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def frame_type(self) -> Type[FrameABC]:
        pass

    @property
    @abstractmethod
    def assets_directory(self) -> str:
        pass

    @property
    @abstractmethod
    def user_control_types(self) -> 'UserControlContainer':
        pass

    @classmethod
    @abstractmethod
    def init(cls):
        pass

    @classmethod
    @abstractmethod
    def ready(cls):
        pass
