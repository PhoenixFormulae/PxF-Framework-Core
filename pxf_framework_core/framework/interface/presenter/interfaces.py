# Standard imports
from typing import List, Type
from abc import ABC, abstractmethod

# System imports
from pxf_framework_core.framework.interface.view.interfaces import ViewABC

# Local imports


class PresenterABC(ABC):

    @classmethod
    @property
    @abstractmethod
    def view_types(cls) -> List[Type[ViewABC]]:
        ...

    @property
    @abstractmethod
    def views(self) -> List[ViewABC]:
        pass

    @classmethod
    @abstractmethod
    def register_view(cls, view: Type[ViewABC]):
        pass

    @classmethod
    @abstractmethod
    def ready(cls):
        pass
