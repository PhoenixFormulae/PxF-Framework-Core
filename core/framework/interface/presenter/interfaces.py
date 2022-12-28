# Standard imports
from typing import List
from abc import ABC, abstractmethod

# System imports
from core.framework.interface.view.interfaces import ViewABC


# Local imports


class PresenterABC(ABC):

    @property
    @abstractmethod
    def view_types(self) -> List[type[ViewABC]]:
        pass

    @property
    @abstractmethod
    def views(self) -> List[ViewABC]:
        pass

    @classmethod
    @abstractmethod
    def register_view(cls, view: ViewABC):
        pass

    @classmethod
    @abstractmethod
    def ready(cls):
        pass
