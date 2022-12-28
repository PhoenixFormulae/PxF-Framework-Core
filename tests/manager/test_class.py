# Standard imports
import unittest
from typing import Type

from core.framework.interface.frame.interfaces import FrameABC
from core.framework.interface.presenter.interfaces import PresenterABC
# Library imports

# External imports
from core.framework.manager.interfaces import ManagerABC
from core.framework.manager.decorators import register_manager
from core.framework.system.data import GameSystemConfiguration
from core.framework.system.interfaces import GameSystemABC


class ManagerTestCase(unittest.TestCase):

    @staticmethod
    def test_define_class():
        class TestSystem(GameSystemABC):
            frames: list[Type[FrameABC]] = []
            manager_types: list[Type[ManagerABC]] = []
            presenter_types: list[Type[PresenterABC]] = []

            configuration: GameSystemConfiguration = None

            def ready(self):
                pass

            def init_interface(self):
                pass

            @classmethod
            def register_manager(cls, manager_type: Type[ManagerABC]):
                pass

            @classmethod
            def register_presenter(cls, presenter_type: Type[PresenterABC]):
                pass

        @register_manager(TestSystem)
        class Test(ManagerABC): # noqa

            @classmethod
            def ready(cls):
                pass


if __name__ == '__main__':
    unittest.main()
