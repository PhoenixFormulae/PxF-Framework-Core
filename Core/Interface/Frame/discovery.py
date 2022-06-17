## System imports
import os
import pkgutil
from importlib import util
from typing import MutableSequence


## Application Imports


## Library Imports
from Core.System.interfaces import GameSystemInterface
from Core.Interface.Set.discovery import import_submodules, discover_interface_sets, discover_interface_sets_data


def discover_frames_data(system: GameSystemInterface, path: str):
	for frame_name in os.listdir(path):
		
		current_frame = None
		for frame in system.Frames:
			if frame_name.lower() == frame.Type.lower():
				current_frame = frame
				break
		
		if current_frame:
			discover_interface_sets_data(current_frame, f'{path}/{frame_name}/Sets/')


def discover_frames(system: GameSystemInterface, path: MutableSequence[str]):
	for importer, name, is_package in pkgutil.iter_modules(path):
		if not is_package:
			continue
		
		current_frame = None
		for frame in system.Frames:
			if frame.Type == name:
				current_frame = frame
				break
		
		if not current_frame:
			continue
		
		current_frame.ControlTypes.DiscoverTypes(current_frame, path)
		current_frame.UserControlTypes.DiscoverTypes(path)
		
		discover_interface_sets(current_frame, [f'{path[0]}/{name}/'])
		
		package_spec = importer.find_spec(name)
		package = util.module_from_spec(package_spec)
		
		import_submodules(package)
	
