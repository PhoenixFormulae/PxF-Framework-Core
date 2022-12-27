## framework imports
import sys
import glob
import pkgutil
from importlib import util
from typing import List, Type, MutableSequence


## Application imports


## Library imports
from core.framework import factory
from core.framework import UserControlLoader
from core.framework import UserControlInterface


def load_user_control_scripts(directory: str):
	user_controls: List[UserControlInterface] = []
	
	for file in glob.glob(f'{directory}/**/*.json', recursive=True):
		user_control: UserControlInterface | None = UserControlLoader.Load(file)
		
		if user_control:
			user_controls.append(user_control)
	
	return user_controls


def get_user_controls(package_path: MutableSequence[str]) -> List[Type[UserControlInterface]]:
	
	user_controls: List[Type[UserControlInterface]] = []
	
	for importer, module_name, is_package in pkgutil.iter_modules(package_path):
		if not is_package:
			continue
		
		package_spec = importer.find_spec(module_name)
		package = util.module_from_spec(package_spec)
		sys.modules[module_name] = package
		package_spec.loader.exec_module(package)
		
		control_names = factory.names_factory(package.__package__)
		
		for control_name in control_names():
			control_factory = factory.get_factory(package.__package__)
			
			control = control_factory(control_name)
			
			if issubclass(control, UserControlInterface):
				user_controls.append(control)
	
	return user_controls
