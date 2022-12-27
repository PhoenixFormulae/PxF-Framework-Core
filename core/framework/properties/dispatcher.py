## framework imports
from typing import Callable


## Application imports
from core.framework import Property

## Library imports


cached_properties: dict = {}
cached_cls_properties: dict = {}


class PropertiesEventDispatcher:
	
	def __init__(self):
		self._properties: dict[str, Property] = {}
		
		self.__register_properties()
	
	def __register_properties(self):
		__cls__ = self.__class__
		
		if __cls__ not in cached_properties:
			attrs_found = cached_properties[__cls__] = {
				name: prop
				for cls in reversed(__cls__.__mro__)
				for name, prop in cached_cls_properties.get(cls, {}).items()
			}
		else:
			attrs_found = cached_properties[__cls__]
		
		self._properties = attrs_found
	
	def bind(self, property_name: str, observer: Callable, instance: object):
		target_property = None
		
		for name, prop in self._properties.items():
			if name == property_name:
				target_property = prop
		
		if not target_property:
			raise AttributeError(f"Cannot find property named '{property_name}'")
			
		target_property.bind(observer, instance)
	
	def refresh(self, property_name: str, observer: Callable, instance: object):
		target_property = None
		
		for name, prop in self._properties.items():
			if name == property_name:
				target_property = prop
		
		if not target_property:
			raise AttributeError(f'Cannot find property named {property_name}')
		
		target_property.dispatch(target_property.get())
