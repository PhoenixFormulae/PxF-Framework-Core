# System imports
from typing import Type
from abc import ABC, abstractmethod

# Local imports
from pxf_framework_core.framework.manager.interfaces import ManagerABC
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.presenter.interfaces import PresenterABC
from pxf_framework_core.framework.system.data import GameSystemConfiguration

# External imports


class GameSystemABC(ABC):

    @property
    @abstractmethod
    def configuration(self) -> GameSystemConfiguration:
        pass

    @property
    @abstractmethod
    def frames(self) -> list[Type[FrameABC]]:
        pass

    @property
    @abstractmethod
    def manager_types(self) -> list[Type[ManagerABC]]:
        pass

    @property
    @abstractmethod
    def presenter_types(self) -> list[Type[PresenterABC]]:
        pass

    @abstractmethod
    def ready(self):
        pass

    @abstractmethod
    def init_interface(self):
        pass

    @classmethod
    @abstractmethod
    def register_manager(cls, manager_type: Type[ManagerABC]):
        pass

    @classmethod
    @abstractmethod
    def register_presenter(cls, presenter_type: Type[PresenterABC]):
        pass
