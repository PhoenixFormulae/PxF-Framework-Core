# Standard imports
from typing import Type

# Local imports
from core.framework.system.interfaces import GameSystemABC
from core.framework.interface.presenter.interfaces import PresenterABC


# External imports


def register_presenter(game_system: Type[GameSystemABC]):
    def decorator(cls: Type[PresenterABC]):
        game_system.register_presenter(cls)

        return cls

    return decorator
