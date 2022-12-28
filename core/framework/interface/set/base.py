# Standard Imports
from abc import ABC

# Local Imports
from core.framework.interface.set.interfaces import InterfaceSetABC


# External Imports


class BaseInterfaceSet(InterfaceSetABC, ABC):
    @classmethod
    def Ready(cls):
        pass
