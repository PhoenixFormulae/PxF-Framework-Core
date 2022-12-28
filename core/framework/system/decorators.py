# System imports
from typing import Type

# Local imports
from core.framework import CoreSystem
from core.framework.system.interfaces import GameSystemABC


# External imports


def register_game_system():
    def decorator(game_system: Type[GameSystemABC]):
        CoreSystem.register_game_system(game_system)

        return game_system

    return decorator
