## framework imports
from abc import ABC
from typing import MutableSequence


## Application imports
from core.framework import CoreSystem
from core.framework import PluginInterface
from core.framework import discover_frames, discover_frames_data


## Library imports


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
	
