# System imports
from typing import Type

# Local imports
from pxf_framework_core.framework.manager.interfaces import ManagerABC
from pxf_framework_core.framework.system.interfaces import GameSystemABC

# External imports


def register_manager(system: Type[GameSystemABC]):
    def decorator(manager: Type[ManagerABC]):
        system.register_manager(manager)

        return manager

    return decorator
