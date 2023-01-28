# Standard Imports
from pathlib import Path

# Local Imports
from pxf_framework_core.framework.interface.view.user_control.base import BaseUserControl
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.parsers.interface.user_control.formats.json import UserControlData

# External Imports


class UserControlLoader:

    @staticmethod
    def load(path: str) -> UserControlABC:
        script_path = Path(path)
        script_json = script_path.read_text()

        data = UserControlData.from_json(script_json)

        return BaseUserControl(data)
