# Standard Imports
from typing import List, Type

from Content.Interface.Frames.Types.Tkinter.Window import TkinterWindow
# Local Imports
from Content.Interface.Types.Tkinter import Controls
from core.framework.interface.data import BaseWindowConfiguration

# External Imports
from core.framework.interface.frame.base import BaseFrame
from core.framework.interface.frame.interfaces import FrameWindowInterface
from core.framework.interface.set.interfaces import InterfaceSetABC
from core.framework.interface.view.user_control.interfaces import UserControlABC
from core.framework.interface.view.control import discovery
from core.framework.interface.view.control.interfaces import ControlABC
from core.framework.interface.view.interfaces import ViewABC


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
    def windows(self) -> List[FrameWindowInterface]:
        return self.__windows

    @property
    def control_types(self) -> List[ControlABC]:
        return self.__controls

    @property
    def user_control_types(self) -> List[UserControlABC]:
        return self.__user_controls

    @property
    def window_type(self) -> type(FrameWindowInterface):
        return self.__window_type

    def __init__(self):
        super().__init__()

        self.__views: List[ViewABC] = []
        self.__window_configuration = BaseWindowConfiguration()
        self.__windows: List[TkinterWindow] = []

        self.__controls: List[ControlABC] = []
        self.__user_controls: List[UserControlABC] = []

        self.__window_type: Type[FrameWindowInterface] = TkinterWindow

    def init(self):
        self.__controls = discovery.get_controls(Controls.__path__)
        self.__windows.append(TkinterWindow(self, self.__window_configuration))

    def loop(self):
        if len(self.__windows) > 0:
            self.__windows[0].Loop()
