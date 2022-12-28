# Standard Imports
from abc import ABC
from typing import MutableSequence

# Local Imports
from core.framework import CoreSystem
from core.framework.interface.frame.discovery import discover_frames_data, discover_frames
from core.framework.plugins.interfaces import PluginABC


# External Imports


class BasePlugin(PluginABC, ABC):

    @property
    def assets_dir(self) -> str:
        return f'{self.__path}/Assets/'

    @property
    def locale_dir(self) -> str:
        return f'{self.assets_dir}/Locale/'

    @property
    def interface_dir(self) -> str:
        return f'{self.assets_dir}/Interface/'

    def __init__(self, path: MutableSequence[str]):
        self.__path = path[0]

        discover_frames_data(CoreSystem.GameSystem, f'{self.interface_dir}/Frames/')
        # discover_interface_data(CoreSystem.GameSystem, f'{self.InterfaceDirectory}/Frames/')
        discover_frames(CoreSystem.GameSystem, self.frames_path)

    def init(self):
        pass

    def ready(self):
        pass
