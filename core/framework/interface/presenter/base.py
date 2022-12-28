# Standard Imports
from abc import ABC

# Local Imports
from core.framework.interface.presenter.interfaces import PresenterABC
from core.framework.interface.view.interfaces import ViewABC

# External Imports


class BasePresenter(PresenterABC, ABC):

    _protocol = None

    @classmethod
    def register_view(cls, view: type[ViewABC]):
        if view not in cls.views:
            cls.view_types.append(view)

    @classmethod
    def ready(cls):
        for view_type in cls.view_types:
            cls.views.append(view_type())
