# System imports
from typing import Type

# Local imports
from pxf_framework_core.framework import CoreSystem
from pxf_framework_core.framework.system.interfaces import GameSystemABC

# External imports


def register_game_system():
    def decorator(game_system: Type[GameSystemABC]):
        CoreSystem.register_game_system(game_system)

        return game_system

    return decorator
