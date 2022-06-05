## System Imports
from functools import wraps
from typing import List, Tuple, Type


## Application Imports
from Core.Interface.Presenter.interfaces import PresenterInterface
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.View.Control.metaclasses import EDITABLE_ATTRIBUTE_NAME, PROPERTY_ATTRIBUTE_NAME, \
	OPTIONAL_ATTRIBUTE_NAME


## Library Imports


def register_view(presenter: Type[PresenterInterface]):
	
	@wraps
	def decorator(cls: ViewInterface):
		
		presenter.RegisterView(cls)
		
		return cls
	
	return decorator


def generic_property(types: str | List[Tuple], editable: bool = False, optional: bool = False):
	
	def decorator(func):
		setattr(func, PROPERTY_ATTRIBUTE_NAME, True)
		setattr(func, EDITABLE_ATTRIBUTE_NAME, editable)
		setattr(func, OPTIONAL_ATTRIBUTE_NAME, optional)
		
		func.property_types_list = []
		
		for arg in types:
			func.property_types_list.append(arg)
		
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			func(*args, **kwargs)
		
		return func_wrapper
	
	return decorator

