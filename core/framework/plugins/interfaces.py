# Standard Imports
from abc import ABC, abstractmethod


# Local Imports


# External Imports


class PluginABC(ABC):

    @property
    @abstractmethod
    def frames_path(self) -> str:
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def ready(self):
        pass
