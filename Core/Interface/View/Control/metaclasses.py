## System Imports
from abc import ABCMeta


## Application Imports


## Library Imports


# Control Attribute Names
PROPERTY_ATTRIBUTE_NAME = "_property"
PROPERTY_NAME_ATTRIBUTE_NAME = "_name"

EDITABLE_ATTRIBUTE_NAME = "_editable"
OPTIONAL_ATTRIBUTE_NAME = "_optional"
MANDATORY_ATTRIBUTE_NAME = "_mandatory"

# Control Attribute List Names
EDITABLE_ATTRIBUTE_LIST_NAME = "editable_list"
PROPERTY_ATTRIBUTE_LIST_NAME = "property_list"
OPTIONAL_ATTRIBUTE_LIST_NAME = "optional_list"
MANDATORY_ATTRIBUTE_LIST_NAME = "mandatory_list"


class ControlMeta(type):
	@classmethod
	def __prepare__(mcs, name: str, bases: tuple):
		return super(ControlMeta, mcs).__prepare__(name, bases)
	
	def __new__(mcs, name: str, bases: tuple, dct):
		if len(bases) > 0:
			mcs.__determine_property_function(PROPERTY_ATTRIBUTE_NAME, PROPERTY_ATTRIBUTE_LIST_NAME, bases[0], dct)
			mcs.__determine_property(OPTIONAL_ATTRIBUTE_NAME, OPTIONAL_ATTRIBUTE_LIST_NAME, dct)
			mcs.__determine_property(MANDATORY_ATTRIBUTE_NAME, MANDATORY_ATTRIBUTE_LIST_NAME, dct)
			mcs.__determine_property(EDITABLE_ATTRIBUTE_NAME, EDITABLE_ATTRIBUTE_LIST_NAME, dct)
			mcs.__gather_properties(dct)
		
		return super(ControlMeta, mcs).__new__(mcs, name, bases, dct)
	
	@staticmethod
	def __determine_property_function(attr_name: str, attr_list_name: str, base, dct: dict):
		# Create custom attribute list
		if attr_list_name not in dct:
			dct[attr_list_name] = {}
		
		dct["parent_cls"] = base
		
		# Add attributes that are marked as specified attribute
		for attr, val in dct.items():
			if hasattr(val, attr_name):
				dct[attr_list_name][val.property_types_list[0]] = val
	
	@staticmethod
	def __determine_property(attr_name: str, attr_list_name: str, dct: dict):
		# Create custom attribute list
		if attr_list_name not in dct:
			dct[attr_list_name] = []
		
		# Add attributes that are marked as specified attribute
		for attr, val in dct.items():
			if hasattr(val, attr_name):
				for prop in val.property_types_list:
					dct[attr_list_name].append(prop)
	
	@staticmethod
	def __gather_properties(dct: dict):
		if 'named_properties' not in dct:
			dct['named_properties'] = {}
			
			for key, val in dct['named_properties'].items():
				if key not in dct['named_properties']:
					dct['named_properties'][key] = val
		
		if 'named_optionals' not in dct:
			dct['named_optionals'] = []
		
		for optional in dct['named_optionals']:
			opt_val = ()
			
			if type(optional) == str:
				opt_val = (optional,)
			elif type(optional) == tuple:
				for opt in optional:
					opt_val += (opt,)
			
			for op in opt_val:
				if op not in dct['named_optionals']:
					dct['named_optionals'].append(op)
		
		if 'named_required' not in dct:
			dct['named_required'] = []
		
		for mandatory in dct['named_required']:
			mand_val = ()
			
			if type(mandatory) == str:
				mand_val = (mandatory,)
			elif type(mandatory) == tuple:
				for mand in mandatory:
					mand_val += (mand,)
			
			for ma in mand_val:
				if ma not in dct['named_optionals']:
					dct['named_optionals'].append(ma)
			
			if mandatory not in dct['named_required']:
				dct['named_required'].append(mandatory)


ControlMetaInterfaceMixin = type('ControlMetaInterfaceMixin', (ABCMeta, ControlMeta), {})
