# Standard Imports
from abc import ABC
from pathlib import Path
from typing import Optional, List

# Local Imports
from pxf_framework_core.framework.interface.view.interfaces import ViewABC
from pxf_framework_core.framework.interface.view.event.interfaces import EventABC
from pxf_framework_core.framework.interface.view.event.base import EventContainer
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.loader import ViewLoader

# External Imports


class BaseView(ViewABC, ABC):

    @property
    def controls(self) -> List[ControlABC]:
        return self.__controls

    @property
    def events(self) -> EventContainer | None:
        return self.__event_container

    def __init__(self):
        super().__init__()

        self.__controls: List[ControlABC] = []
        self.__events: List[EventABC] = []

        self.__event_container: EventContainer | None = None  # EventContainer(events.__path__)

        self.__path: str | None = None
        self.__loaded: bool = False

        self.__view_loader = ViewLoader(self, self.frame_type, self.interface_set_type)

    def ready(self):
        pass

    def _prepare(self):
        pass

    def _load(self, path: str):
        if self.__loaded:
            raise Exception('view was already loaded, cannot load again')

        self.__path = Path(path)

        self.__view_loader.load(self.__path)
        self.__loaded = True

        self.hide()

    def show(self):
        # TODO: Showing root level controls should be enough to show the view as it would not be necessary to
        #       alter the final desired state of children visibility
        for control in self.__controls:
            control.show()

    def hide(self):
        for control in self.__controls:
            control.hide()

    def add_control(self, control: ControlABC):
        if control not in self.__controls:
            self.__controls.append(control)

    def find_control(self, control_name: str, recursive: bool = True) -> Optional[ControlABC]:
        for control in self.__controls:
            if control.name == control_name:
                return control

            if recursive:
                return control.find_child(control_name)

        return None

    def OnPreLoad(self):
        pass

    def OnLoad(self):
        if self.__loaded:
            return

        for control in self.__controls:
            self.call_child(control, 'OnViewLoad')

        self.__loaded = True

    def OnPostLoad(self):
        for control in self.__controls:
            self.call_child(control, 'OnViewPostLoad')

    @staticmethod
    def call_child(control: ControlABC, name: str):
        if not hasattr(control, name):
            return

        call = getattr(control, name)

        if callable(call):
            call()
