## System Imports


## Application Imports


## Library Imports
from Core.Interface.View.Control.interfaces import ControlInterface


class ControlNotFoundException(Exception):
	
	def __init__(self, control_type: str):
		self.control_type = control_type
	
	def __str__(self):
		return f"Control '{self.control_type}' was not found on registered controls."


class IncompleteControlException(Exception):
	
	def __init__(self, control_type: str, missing_properties: dict):
		self.control_type = control_type
		self.missing_properties = missing_properties
	
	def __str__(self):
		build_str = f"Control '{self.control_type}' required properties were not fulfilled:"
		
		for key, val in self.missing_properties.items():
			build_str += f"\n  - {key} : {type(val).__name__}"
		
		return build_str


class IncompleteControlListException(Exception):
	
	def __init__(self, control: ControlInterface, missing_properties: list):
		self.control = control
		self.missing_properties = missing_properties
	
	def __str__(self):
		build_str = f"Control '{self.control.type}' AKA '{type(self.control).__name__}'" \
		            f" required properties were not fulfilled:"
		
		for key in self.missing_properties:
			build_str += f"\n  - {key}"
		
		return build_str


# TODO: Check if this is possible in a minimalistic way later
class ControlIncompleteExceptionTODO(Exception):
	
	@staticmethod
	def name_of_object(arg):
		# check __name__ attribute (functions)
		try:
			return arg.__name__
		except AttributeError:
			pass
		
		for name, value in globals().items():
			if value is arg and not name.startswith('_'):
				return name
	
	def __init__(self, control_type: str, missing_properties: dict):
		self.control_type = control_type
		self.missing_properties = missing_properties
	
	def __str__(self):
		build_str = f"Control '{self.control_type}' required properties were not fulfilled:"
		
		for missing_property in self.missing_properties:
			str_var = self.name_of_object(missing_property)
			str_type = type(missing_property).__name__
			
			build_str += f"\n  - {str_var} : {str_type}"
		
		return build_str


class ControlInvalidException(Exception):
	
	def __init__(self, control_type: str):
		self.control_type = control_type
	
	def __str__(self):
		return f"Control '{self.control_type}' is an invalid registered control."


if __name__ == "__main__":
	x = 1
	y = 1
	
	control_missing_properties_dict = {
		'x': x,
		'y': y
	}
	
	raise IncompleteControlException("Button", control_missing_properties_dict)
