# Standard Imports
from pathlib import Path
from typing import Type

# Local Imports
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.set.interfaces import InterfaceSetABC
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.control.loader import ControlLoader
from pxf_framework_core.framework.interface.view.interfaces import ViewABC
from pxf_framework_core.framework.parsers.interface.view.formats.json import ViewData

# External Imports


class ViewLoader:
    def __init__(self, view: ViewABC, frame: Type[FrameABC], interface_set: Type[InterfaceSetABC]):
        self.__view = view
        self.__frame_type = frame
        self.__interface_set_type = interface_set

        self.__control_loader = ControlLoader(self.__frame_type, self.__interface_set_type, view)
        self.__indent = 1

    def load(self, path: Path) -> ViewABC:
        script_json = path.read_text()
        view_data = ViewData.from_json(script_json)

        self.__load_script(view_data)

        return self.__view

    def __load_script(self, data: ViewData):
        view_root: ControlABC = self.__frame_type.base_control_type

        self.__control_loader.load_control_properties(view_root, data.to_dict())

        self.__view.add_control(view_root)
