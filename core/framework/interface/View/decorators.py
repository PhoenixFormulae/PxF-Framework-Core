## framework imports
from functools import wraps
from typing import List, Tuple, Type


## Application imports
from core.framework import PresenterInterface
from core.framework import ViewInterface
from core.framework import EDITABLE_ATTRIBUTE_NAME, PROPERTY_ATTRIBUTE_NAME, \
	REQUIRED_ATTRIBUTE_NAME


## Library imports


def register_view(presenter: Type[PresenterInterface]):
	
	def decorator(cls: ViewInterface):
		
		presenter.RegisterView(cls)
		
		return cls
	
	return decorator


def generic_property(types: str | List[Tuple], editable: bool = False, required: bool = True):
	
	def decorator(func):
		setattr(func, PROPERTY_ATTRIBUTE_NAME, True)
		setattr(func, EDITABLE_ATTRIBUTE_NAME, editable)
		setattr(func, REQUIRED_ATTRIBUTE_NAME, required)
		
		func.property_types_list = []
		
		if isinstance(types, str):
			func.property_types_list.append(types)
		elif isinstance(types, list):
			for arg in types:
				func.property_types_list.append(arg)
		else:
			raise AttributeError('Expected types to be either a string or a list')
		
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			func(*args, **kwargs)
		
		return func_wrapper
	
	return decorator

