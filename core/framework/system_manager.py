# System imports

# Local imports
from core.framework.manager.interfaces import ManagerABC


# External imports


class SystemManager(ManagerABC):

    @classmethod
    def ready(cls):
        from core.framework import CoreSystem
        CoreSystem.GameSystem.init_interface()
