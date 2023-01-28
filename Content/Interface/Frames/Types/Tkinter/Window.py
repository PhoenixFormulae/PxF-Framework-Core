# Standard imports
import tkinter
from typing import Optional

# Local imports
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.frame.window.abc import FrameWindowABC
from pxf_framework_core.framework.interface.frame.window.data import FrameWindowConfig


# External imports


class TkinterWindow(FrameWindowABC):

    def __init__(self, frame: FrameABC, frame_configuration: FrameWindowConfig):
        super().__init__()

        self.__frame = frame

        self.__window_configuration = frame_configuration

        self.__window: Optional[tkinter.Tk] = self.create()

    def __del__(self):
        pass

    def create(self) -> tkinter.Tk:
        window = tkinter.Tk()
        window.title(self.__window_configuration.title)
        window.geometry(f"{self.__window_configuration.width}x{self.__window_configuration.height}")
        window.attributes('-fullscreen', not self.__window_configuration.windowed)

        return window

    def loop(self):
        self.__window.mainloop()
