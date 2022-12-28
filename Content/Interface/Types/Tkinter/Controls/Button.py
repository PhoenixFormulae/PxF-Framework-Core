# Standard Imports
import tkinter

# Local Imports
from Content.Interface.Frames.Types.Tkinter.View.control import Control

# External Imports


class Button(Control, tkinter.Button):

    kind = 'button'

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

    def __init__(self, parent):
        super(tkinter.Button, self).__init__(parent, self.kind)
        super(Control).__init__()

    def __del__(self):
        super(tkinter.Button, self).destroy()

    def show(self):
        pass

    def hide(self):
        pass

