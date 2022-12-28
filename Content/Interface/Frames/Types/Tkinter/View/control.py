# Standard Imports
from typing import List
from tkinter import ttk

# Local Imports
from core.framework.interface.view.control.interfaces import ControlABC
from core.framework.interface.view.control.metaclasses import ControlMetaABCMixin
from core.framework.interface.view.user_control.interfaces import UserControlABC
from core.framework.interface.view.event.interfaces import EventABC


# External Imports


class Control(ControlABC, ttk.Widget):

    kind: str = "control"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def children(self) -> List[ControlABC]:
        return self.__children

    @property
    def user_controls(self) -> List:
        return self.__user_controls

    @property
    def width(self) -> int:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError

    @property
    def global_position(self) -> tuple[int, int]:
        raise NotImplementedError

    @property
    def required_properties(self) -> list[str]:
        raise NotImplementedError

    @property
    def optional_properties(self) -> list[str]:
        raise NotImplementedError

    def __init__(self):
        super().__init__()

        self.__name = ''
        self.__children = []

        self.__controls = []
        self.__user_controls = []

    def __del__(self):
        super(ttk.Widget, self).destroy()

    def add_child(self, control: ControlMetaABCMixin):
        pass

    def add_children(self, controls: List[ControlMetaABCMixin]):
        pass

    def find_child(self, child_name: str) -> ControlMetaABCMixin | None:
        pass

    def add_user_control(self, user_control: UserControlABC | List[UserControlABC]):
        pass

    def set_parent(self, parent: ControlMetaABCMixin):
        pass

    def add_event(self, event: EventABC):
        pass

    def validated(self):
        pass

    def validate(self):
        pass

    def invalidate(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass
