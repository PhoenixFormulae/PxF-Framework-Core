## System Imports
import sys
import pkgutil
from importlib import util
from typing import List, MutableSequence, Type


## Application Imports
from Core.Plugins import factory
from Core.Interface.View.Control.interfaces import ControlInterface
from Core.Interface.View.Control.exceptions import ControlNotFoundException, ControlInvalidException
from Core.Interface.View.UserControl.interfaces import UserControlInterface


## Library Imports


def get_control(package_path: list[str], type_name: str):
	"""
	Searches for a control in a given package module path
	that matches the specified given type name

	:param: package_path: The package module path to search in
	:param: type_name: The name of the control type
	:return: The control class
	"""
	
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
			# print(f"Control type: {control.Type}")
			
			if control.type == type_name:
				if not issubclass(control, ControlInterface):
					raise ControlInvalidException(control_name)
				
				return control
	
	raise ControlNotFoundException(type_name)


def get_controls(package_path: MutableSequence[str]) -> List[Type[ControlInterface]]:
	"""
	Searches for all controls in a given package module path
	that are registered in the factory

	:param: package_path: The package module path to search in
	:return: The list of control classes
	"""
	
	controls: List[Type[ControlInterface]] = []
	
	for importer, module_name, is_package in pkgutil.iter_modules(package_path):
		if not is_package:
			continue
		
		spec = importer.find_spec(module_name)
		module = util.module_from_spec(spec)
		sys.modules[module_name] = module
		spec.loader.exec_module(module)
		
		control_names = factory.names_factory(module.__package__)
		
		for control_name in control_names():
			control_factory = factory.get_factory(module.__package__)
			
			# TODO: Maybe add type checking to be sure that the class is based of ControlInterface
			#       just like in the get_control method above
			control = control_factory(control_name)
			
			controls.append(control)
	
	return controls

