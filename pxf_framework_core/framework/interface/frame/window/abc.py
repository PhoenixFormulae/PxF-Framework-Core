# Standard Imports
from abc import ABC, abstractmethod

# Local Imports

# External Imports


class FrameWindowABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def loop(self):
        pass

