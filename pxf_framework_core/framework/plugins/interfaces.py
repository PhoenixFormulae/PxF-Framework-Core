# Standard Imports
from abc import ABC, abstractmethod
from typing import MutableSequence

# Local Imports

# External Imports


class PluginABC(ABC):

    @property
    @abstractmethod
    def frames_path(self) -> MutableSequence[str]:
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def ready(self):
        pass
