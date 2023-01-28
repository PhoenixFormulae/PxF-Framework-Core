# Standard Imports
from abc import ABC
from typing import Type

# Local Imports
from pxf_framework_core.framework.interface.view.interfaces import ViewABC
from pxf_framework_core.framework.interface.presenter.interfaces import PresenterABC

# External Imports


class BasePresenter(PresenterABC, ABC):

    _protocol = None

    @classmethod
    def register_view(cls, view: Type[ViewABC]):
        if view not in cls.views:
            cls.view_types.append(view)

    @classmethod
    def ready(cls):
        for view_type in cls.view_types:
            cls.views.append(view_type())
