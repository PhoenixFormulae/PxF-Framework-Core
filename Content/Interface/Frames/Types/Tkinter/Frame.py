# Standard Imports
from typing import List, Type

# Local Imports
from Content.Interface.Types.Tkinter import Controls
from Content.Interface.Frames.Types.Tkinter.Window import TkinterWindow

# External Imports
from pxf_framework_core.framework.interface.frame.base import BaseFrame
from pxf_framework_core.framework.interface.frame.window.abc import FrameWindowABC
from pxf_framework_core.framework.interface.frame.window.data import FrameWindowConfig
from pxf_framework_core.framework.interface.set.interfaces import InterfaceSetABC
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.interface.view.control import discovery
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.interfaces import ViewABC


class TkinterFrame(BaseFrame):
    kind: str = "Tkinter"
    static_window: bool = False

    @property
    def assets_dir(self) -> str:
        raise NotImplementedError

    @property
    def interface_sets(self) -> list[Type[InterfaceSetABC]]:
        raise NotImplementedError

    @property
    def base_control_type(self) -> Type[ControlABC]:
        raise NotImplementedError

    @property
    def event_types(self):
        raise NotImplementedError

    @property
    def views(self) -> List[ViewABC]:
        return self.__views

    @property
    def windows(self) -> List[FrameWindowABC]:
        return self.__windows

    @property
    def control_types(self) -> List[ControlABC]:
        return self.__controls

    @property
    def user_control_types(self) -> List[UserControlABC]:
        return self.__user_controls

    @property
    def window_type(self) -> type(FrameWindowABC):
        return self.__window_type

    def __init__(self):
        super().__init__()

        self.__views: List[ViewABC] = []
        self.__window_configuration = FrameWindowConfig()
        self.__windows: List[TkinterWindow] = []

        self.__controls: List[ControlABC] = []
        self.__user_controls: List[UserControlABC] = []

        self.__window_type: Type[FrameWindowABC] = TkinterWindow

    def init(self):
        self.__controls = discovery.get_controls(Controls.__path__)
        self.__windows.append(TkinterWindow(self, self.__window_configuration))

    def loop(self):
        if len(self.__windows) > 0:
            self.__windows[0].loop()
