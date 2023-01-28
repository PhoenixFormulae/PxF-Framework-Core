# Standard imports

# Local imports
from .manager.interfaces import ManagerABC
from . import CoreSystem

# External imports


class SystemManager(ManagerABC):

    @classmethod
    def ready(cls):
        CoreSystem.GameSystem.init_interface()
