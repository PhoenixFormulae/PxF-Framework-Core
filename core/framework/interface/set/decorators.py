# System imports
from typing import Type

# Local imports
from core.framework.interface.frame.interfaces import FrameABC
from core.framework.interface.set.interfaces import InterfaceSetABC


# External imports


def register_interface_set(frame: Type[FrameABC]):
    def decorator(cls: Type[InterfaceSetABC]):
        frame.register_interface_set(cls)

        return cls

    return decorator
