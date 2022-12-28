# Standard Imports
from pathlib import Path

# Local Imports
from core.framework.interface.frame.interfaces import FrameABC
from core.framework.interface.set.interfaces import InterfaceSetABC
from core.framework.interface.view.control.loader import ControlLoader
from core.framework.interface.view.interfaces import ViewABC
from core.framework.parsers.interface.view.formats.json import ViewData

# External Imports


class ViewLoader:
    def __init__(self, view: ViewABC, frame: FrameABC, interface_set: InterfaceSetABC):
        self.__view = view
        self.__frame = frame
        self.__interface_set = interface_set

        self.__control_loader = ControlLoader(self.__frame, self.__interface_set, view)
        self.__indent = 1

    def Load(self, path: str) -> ViewABC:
        script_path = Path(path)
        script_json = script_path.read_text()
        view_data = ViewData.from_json(script_json)

        self.__LoadScript(view_data)

        return self.__view

    def __LoadScript(self, data: ViewData):
        view_root = self.__frame.base_control_type()

        self.__control_loader.LoadControlProperties(view_root, data.to_dict())

        self.__view.add_control(view_root)
