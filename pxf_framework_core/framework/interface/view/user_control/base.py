# Standard Imports
from pathlib import Path

# Local Imports
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.view.container import Container
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.control.loader import ControlLoader
from pxf_framework_core.framework.interface.view.interfaces import ViewABC
from pxf_framework_core.framework.interface.view.user_control import discovery
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.parsers.interface.user_control.formats.json import UserControlData

# External Imports


class BaseUserControl(UserControlABC):

    @property
    def kind(self) -> str:
        return self._user_control_properties['name']

    @property
    def user_control_properties(self) -> dict:
        return self._user_control_properties

    @property
    def control_properties(self) -> dict:
        return self._control_properties

    @property
    def event_properties(self) -> dict:
        return {}

    def __init__(self, data: UserControlData):
        self._control_properties: dict = {}
        self._user_control_properties: dict = data.to_dict()
        self.__user_control_data = data

    def init(self, frame: FrameABC, view: ViewABC) -> ControlABC:
        control_loader: ControlLoader = ControlLoader(frame, None, view)
        control: ControlABC = control_loader.load_user_control(self.__user_control_data)

        return control


class UserControlContainer(Container[UserControlABC]):

    def __init__(self, path: Path):
        super().__init__(path, discovery.find_user_control_types)

