## System Imports
import pkgutil
from typing import List, MutableSequence


## Application Imports
from Core.Plugins import factory
from Core.Interface.View.Events.interfaces import EventInterface


## Library Imports


def get_events(package_path: MutableSequence[str]) -> List[EventInterface]:
	"""
	Searches for all events in a given package module path
	that are registered in the factory

	:param package_path: The package module path to search in
	:return: The list of event classes
	"""
	
	events: List[EventInterface] = []
	
	for importer, module_name, is_package in pkgutil.iter_modules(package_path):
		if not is_package:
			continue
		
		type_module = importer.find_module(module_name).load_module(module_name)
		
		event_names = factory.names_factory(type_module.__package__)
		
		for event_name in event_names():
			event_factory = factory.get_factory(type_module.__package__)
			
			# TODO: Maybe add type checking to be sure that the class is based of EventInterface
			# just like in the control discovery get_control method does
			event = event_factory(event_name)
			
			events.append(event)
	
	return events
