# System imports
import logging
from typing import Type

# Local imports
from core.framework import plugins
from core.framework.system.interfaces import GameSystemABC
from core.framework.system_manager import SystemManager


# External imports


class CoreSystem:
    GameSystemTypes: list[Type[GameSystemABC]] = []
    GameSystem: GameSystemABC = None
    BootGameSystem: bool = True

    Plugins: None = None

    @classmethod
    def register_game_system(cls, game_system_type: Type[GameSystemABC]):
        if game_system_type not in cls.GameSystemTypes:
            cls.GameSystemTypes.append(game_system_type)

    @classmethod
    def initialize(cls):
        logging.debug('Initializing core framework')

    @classmethod
    def run(cls):
        cls.Plugins = plugins.init()

        if cls.BootGameSystem:
            cls.GameSystem.ready()
        else:
            SystemManager.ready()
