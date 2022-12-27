# Standard imports
import logging
from typing import Type, Dict, Optional, Any, List, Callable


# Library imports


# External imports
from core.framework import simple
from core.framework import unpack_tuples
from core.framework import EventLoader
from core.framework import ViewInterface
from core.framework import FrameInterface
from core.framework import InterfaceSetInterface
from core.framework import ControlInterface
from core.framework import UserControlInterface
from core.framework import IncompleteControlPropertiesException
from core.framework import PROPERTY_ATTRIBUTE_LIST_NAME, REQUIRED_ATTRIBUTE_LIST_NAME


class ControlLoader:
	
	def __init__(self, frame: FrameInterface, interface_set: InterfaceSetInterface, view: ViewInterface | None = None):
		self.__frame: FrameInterface = frame
		self.__interface_set: InterfaceSetInterface = interface_set
		self.__view = view
		
		self.__event_loader = EventLoader(self.__frame)
		self.__indent: int = 1
	
	def Load(self, properties: Dict) -> UserControlInterface | ControlInterface | None:
		is_control = True
		
		if 'type' not in properties:
			raise Exception('No type was provided')
		
		if 'category' in properties:
			if properties['category'] == 'user_control':
				is_control = False
		
		if not is_control:
			return self.LoadUserControl(properties)
		
		return self.LoadControl(properties)
	
	def LoadUserControl(self, properties: dict):
		user_control_type: Type[UserControlInterface] = self.__frame.UserControlTypes.FindType(properties['type'])
		
		if not user_control_type:
			raise FileNotFoundError(f"Could not find user control with the type '{properties['type']}'")
		
		user_control = user_control_type()
		user_control._user_control_properties = properties
		
		for event in self.__event_loader.LoadEvents(user_control.EventProperties):
			self.__view.events.AddEvent(event)
		
		self.LoadControlProperties(user_control, properties)
		
		return user_control
	
	def LoadUserControlInstance(self, user_control: UserControlInterface, properties: dict) -> ControlInterface:
		user_control._control_properties = properties
		
		control: Optional[ControlInterface] = None
		
		control_name = user_control.UserControlProperties['control_type']
		control_type: Optional[type(ControlInterface)] = self.__frame.ControlTypes.FindType(control_name)
		
		if not control_type:
			raise ModuleNotFoundError(f'Could not find control type {control_name}')
		
		control = control_type()
		control.type = user_control.UserControlProperties['name']
		
		# event_loader: EventLoader = EventLoader(self.__frame)
		# for event in event_loader.LoadEvents(user_control.model.events_properties):
		# 	view.AddEvent(event)
		
		# TODO: Decide if user control properties should be loaded here
		# self.LoadControlProperties(control, user_control.UserControlProperties)
		self.LoadControlProperties(control, user_control.ControlProperties)
		
		return control
	
	def LoadControl(self, properties: Dict) -> Optional[ControlInterface]:
		
		control_type: Type[ControlInterface] = self.__frame.ControlTypes.FindType(properties['type'])
		
		if not control_type:
			raise ModuleNotFoundError(f"Could not find control with the type '{properties['type']}'")
		
		control = control_type()
		control.name = properties['name']
		
		self.LoadControlProperties(control, properties)
		
		return control
	
	def LoadControlProperties(self, control: ControlInterface, properties: dict):
		PropertiesLoader.CheckRequiredProperties(control, properties)
		
		control.name = properties['name']
		
		print(f'{"": <{2 * self.__indent}}{control.name} ({type(control).__name__}/{control.Type})')
		
		for key, val in getattr(control, PROPERTY_ATTRIBUTE_LIST_NAME).items():
			if self.__LoadProperty(control, key, properties):
				print(f'{"": <{2 * self.__indent + 2}}- {key}')
			# else:
			# 	print("".ljust(4 * self.__indent) + f"Skipping optional property: {key}")
		
		if 'children' in properties:
			print(f'{"": <{2 * self.__indent + 2}}children:')
			self.__indent += 2
			
			self.__LoadChildren(control, properties['children'])
		
		# if 'events' in properties:
		# 	for event_name in properties['events']:
		#		for event in self.__view.events:
		#			if event.name == event_name:
		#				control.AddEvent(event)
		
		if 'subscribe' in properties:
			PropertiesLoader.AddEventSubscribers(control, properties['subscribe'])
	
	def __LoadChildren(self, control: ControlInterface, children: dict):
		for key, child_properties in children.items():
			child_type = child_properties['type']
			child_properties['name'] = key
			
			control_type = self.__frame.ControlTypes.FindType(child_type)
			user_control_type = self.__interface_set.UserControlTypes.FindType(child_type)
			
			child: ControlInterface | None = None
			
			if control_type:
				child = control_type()
				self.LoadControlProperties(child, child_properties)
			
			elif user_control_type:
				user_control = user_control_type
				child = self.LoadUserControlInstance(user_control, child_properties)
			
			if not child:
				logger = logging.getLogger('core_logger')
				logger.error(f'Cannot find control type {child_type}')
				continue
			
			child.SetParent(control)
			control.AddChild(child)
	
	def __LoadProperty(self, control: ControlInterface, prop_key: Any, properties: dict) -> bool:
		properties_list = getattr(control, PROPERTY_ATTRIBUTE_LIST_NAME)
		required_properties = unpack_tuples(getattr(control, REQUIRED_ATTRIBUTE_LIST_NAME))
		
		prop_keys = ()
		if type(prop_key) == str:
			prop_keys += (prop_key, )
		
		elif type(prop_key) == tuple:
			prop_keys = prop_key
		
		else:
			raise Exception(f"Property key should be 'str' or 'tuple' got '{type(prop_key)}' instead.")
		
		for key in prop_keys:
			if key not in properties:
				return False
		
		bound = False
		property_function = properties_list[prop_key]
		args = (control,)
		for prop in prop_keys:
			prop_val = properties[prop]
			
			if isinstance(prop_val, str):
				if simple.has_expression(prop_val):
					attr = simple.resolve_expression(self.__view, prop_val)
					self.__view.bind(attr, property_function, control)
					self.__view.refresh(attr, property_function, control)
					bound = True
					
			args += (prop_val,)
		
		if len(args) > 1 and not bound:
			property_function(*args)
		
		return True


class PropertiesLoader:
	
	@staticmethod
	def CheckRequiredProperties(control: ControlInterface, properties: dict):
		missing_properties = []
		
		required_properties = unpack_tuples(getattr(control, REQUIRED_ATTRIBUTE_LIST_NAME))
		
		for required_property in required_properties:
			if required_property not in properties:
				missing_properties.append(required_property)
		
		if len(missing_properties) > 0:
			raise IncompleteControlPropertiesException(control, missing_properties)
	
	@staticmethod
	def FindPropertyMethod(control: ControlInterface, properties: List[str]) -> Optional[Callable]:
		properties_dict = PropertiesLoader.ResolvePropertiesMethods(control)
		
		for subscribing_property in properties:
			for props, property_method in properties_dict.items():
				if isinstance(props, tuple):
					match = all([i == j for i, j in zip(props, subscribing_property)])
					
					if match:
						return property_method
		
		return None
	
	@staticmethod
	def ResolvePropertiesMethods(control: ControlInterface):
		current_control_class: ControlInterface = control
		
		properties_dict: Dict = {}
		
		while hasattr(current_control_class, "parent_cls"):
			properties = getattr(current_control_class, PROPERTY_ATTRIBUTE_LIST_NAME)
			for key, val in properties.items():
				if key not in properties_dict:
					properties_dict[key] = val
			
			current_control_class = current_control_class.parent_cls
		
		return properties_dict
	
	@staticmethod
	def AddEventSubscribers(view: ViewInterface, control: ControlInterface, properties: dict):
		for event_name, subscriber_properties in properties.items():
			event = view.events.FindEvent(event_name)
			
			if event:
				subscriber: Optional[Callable] = PropertiesLoader.FindPropertyMethod(control, subscriber_properties)
				
				if not subscriber:
					raise AttributeError(f"Could not find subscriber for event '{event_name}'")
					
				event.AddSubscriber(subscriber)
				event.AddControl(control)
