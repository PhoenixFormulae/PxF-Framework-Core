# Standard Imports
from abc import ABC

# Local Imports

# External Imports
from pxf_framework_core.framework.system.interfaces import GameSystemABC


class BaseGameSystem(GameSystemABC, ABC):

    def ready(self):
        for manager in self.manager_types:
            manager.ready()

        self.ready_presenters()
        self.init_interface()

    def post_ready(self):
        for manager in self.manager_types:
            if hasattr(manager, 'PostReady'):
                manager.PostReady()

        self.init_interface()

    def ready_presenters(self):
        for presenter in self.presenter_types:
            presenter.ready()

    def init_interface(self):
        for frame in self.frames:
            frame.ready()
