# System imports
from abc import ABC, abstractmethod


# Local imports

# External imports


class LocaleContextABC(ABC):

    @abstractmethod
    def string(self, key: str):
        pass

    @abstractmethod
    def int(self, key: str):
        pass


class LocaleABC(ABC):

    @abstractmethod
    def get_context(self, key: str) -> LocaleContextABC:
        pass
