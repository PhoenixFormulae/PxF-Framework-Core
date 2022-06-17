## System Imports
from abc import ABC
from typing import MutableSequence


## Application Imports
from Core import CoreSystem
from Core.Plugins.interfaces import PluginInterface
from Core.Interface.Frame.discovery import discover_frames, discover_frames_data


## Library Imports


class BasePlugin(PluginInterface, ABC):
	
	@property
	def AssetsDirectory(self) -> str:
		return f'{self.__path}/Assets/'
	
	@property
	def LocaleDirectory(self) -> str:
		return f'{self.AssetsDirectory}/Locale/'
	
	@property
	def InterfaceDirectory(self) -> str:
		return f'{self.AssetsDirectory}/Interface/'
	
	def __init__(self, path: MutableSequence[str]):
		self.__path = path[0]
		
		discover_frames_data(CoreSystem.GameSystem, f'{self.InterfaceDirectory}/Frames/')
		# discover_interface_data(CoreSystem.GameSystem, f'{self.InterfaceDirectory}/Frames/')
		discover_frames(CoreSystem.GameSystem, self.FramesPath)
	
	def Initialize(self):
		pass
	
	def Ready(self):
		pass
	
