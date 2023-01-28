# Standard imports
from typing import Type, Dict, Optional, Any, List, Callable

# Local Imports
from pxf_framework_core.framework.expressions import simple
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.set.interfaces import InterfaceSetABC
from pxf_framework_core.framework.interface.view.control.exceptions import IncompleteControlPropertiesException
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.control.metaclasses import PROPERTY_ATTRIBUTE_LIST_NAME, \
    REQUIRED_ATTRIBUTE_LIST_NAME
from pxf_framework_core.framework.interface.view.event.loader import EventLoader
from pxf_framework_core.framework.interface.view.interfaces import ViewABC
from pxf_framework_core.framework.logging import core_logger
from pxf_framework_core.framework.utils.zip import unpack_tuples

# External imports


class ControlLoader:

    def __init__(self, frame: Type[FrameABC], interface_set: Type[InterfaceSetABC] | None, view: ViewABC | None = None):
        self.__frame = frame
        self.__interface_set = interface_set
        self.__view = view

        self.__event_loader = EventLoader(self.__frame)
        self.__indent: int = 1

    def load(self, properties: Dict) -> UserControlABC | ControlABC | None:
        is_control = True

        if 'type' not in properties:
            raise Exception('No type was provided')

        if 'category' in properties:
            if properties['category'] == 'user_control':
                is_control = False

        if not is_control:
            return self.load_user_control(properties)

        return self.load_control(properties)

    def load_user_control(self, properties: dict):
        user_control_type: Type[UserControlABC] = self.__frame.user_control_types.find_type(properties['type'])

        if not user_control_type:
            raise FileNotFoundError(f"Could not find user control with the type '{properties['type']}'")

        user_control = user_control_type()
        user_control._user_control_properties = properties

        for event in self.__event_loader.load_events(user_control.event_properties):
            self.__view.events.add_event(event)

        self.load_user_control_properties(user_control, properties)

        return user_control

    def load_user_control_properties(self, user_control: UserControlABC, properties: dict) -> ControlABC:
        user_control._control_properties = properties

        control_name = user_control.user_control_properties['control_type']
        control_type: Optional[Type[ControlABC]] = self.__frame.control_types.find_type(control_name)

        if not control_type:
            raise ModuleNotFoundError(f'Could not find control type {control_name}')

        control = control_type()
        control.kind = user_control.user_control_properties['name']

        # event_loader: EventLoader = EventLoader(self.__frame)
        # for event in event_loader.LoadEvents(user_control.model.events_properties):
        # 	view.AddEvent(event)

        # TODO: Decide if user control properties should be loaded here
        # self.LoadControlProperties(control, user_control.UserControlProperties)
        self.load_control_properties(control, user_control.control_properties)

        return control

    def load_control(self, properties: Dict) -> Optional[ControlABC]:

        control_type: Type[ControlABC] = self.__frame.control_types.find_type(properties['type'])

        if not control_type:
            raise ModuleNotFoundError(f"Could not find control with the type '{properties['type']}'")

        control = control_type()
        control.name = properties['name']

        self.load_control_properties(control, properties)

        return control

    def load_control_properties(self, control: ControlABC, properties: dict):
        PropertiesLoader.check_required_properties(control, properties)

        control.name = properties['name']

        print(f'{"": <{2 * self.__indent}}{control.name} ({type(control).__name__}/{control.kind})')

        for key, val in getattr(control, PROPERTY_ATTRIBUTE_LIST_NAME).items():
            if self.__load_property(control, key, properties):
                print(f'{"": <{2 * self.__indent + 2}}- {key}')
            # else:
            # 	print(f{"".ljust(4 * self.__indent)}Skipping optional property: {key}")

        if 'children' in properties:
            print(f'{"": <{2 * self.__indent + 2}}children:')
            self.__indent += 2

            self.__load_children(control, properties['children'])

        # if 'events' in properties:
        # 	for event_name in properties['events']:
        #       for event in self.__view.events:
        #           if event.name == event_name:
        #               control.AddEvent(event)

        if 'subscribe' in properties:
            PropertiesLoader.add_event_subscribers(self.__view, control, properties['subscribe'])

    def __load_children(self, control: ControlABC, children: dict):
        for key, child_properties in children.items():
            child_type = child_properties['type']
            child_properties['name'] = key

            control_type = self.__frame.control_types.find_type(child_type)
            user_control_type = self.__interface_set.user_control_types.find_type(child_type)

            child: ControlABC | None = None

            if control_type:
                child = control_type()
                self.load_control_properties(child, child_properties)

            elif user_control_type:
                user_control = user_control_type()
                child = self.load_user_control_properties(user_control, child_properties)

            if not child:
                core_logger.error(f'Cannot find control type {child_type}')
                continue

            child.set_parent(control)
            control.add_child(child)

    def __load_property(self, control: ControlABC, prop_key: Any, properties: dict) -> bool:
        if not self.__view:
            raise AttributeError("No view is set")

        properties_list = getattr(control, PROPERTY_ATTRIBUTE_LIST_NAME)
        # required_properties = unpack_tuples(getattr(control, REQUIRED_ATTRIBUTE_LIST_NAME))

        prop_keys = ()
        if type(prop_key) == str:
            prop_keys += (prop_key, )

        elif type(prop_key) == tuple:
            prop_keys = prop_key

        else:
            raise Exception(f"Property key should be 'str' or 'tuple' got '{type(prop_key)}' instead.")

        key: str
        for key in prop_keys:
            if key not in properties:
                return False

        bound = False
        property_function = properties_list[prop_key]
        args = (control,)

        prop: str
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
    def check_required_properties(control: ControlABC, properties: dict):
        missing_properties = []

        required_properties = unpack_tuples(getattr(control, REQUIRED_ATTRIBUTE_LIST_NAME))

        for required_property in required_properties:
            if required_property not in properties:
                missing_properties.append(required_property)

        if len(missing_properties) > 0:
            raise IncompleteControlPropertiesException(control, missing_properties)

    @staticmethod
    def find_property_method(control: ControlABC, properties: List[str]) -> Optional[Callable]:
        properties_dict = PropertiesLoader.resolve_properties_method(control)

        for subscribing_property in properties:
            for props, property_method in properties_dict.items():
                if isinstance(props, tuple):
                    match = all([i == j for i, j in zip(props, subscribing_property)])

                    if match:
                        return property_method

        return None

    @staticmethod
    def resolve_properties_method(control: ControlABC):
        current_control_class: ControlABC = control

        properties_dict: Dict = {}

        while hasattr(current_control_class, "parent_cls"):
            properties = getattr(current_control_class, PROPERTY_ATTRIBUTE_LIST_NAME)
            for key, val in properties.items():
                if key not in properties_dict:
                    properties_dict[key] = val

            current_control_class = current_control_class.parent_cls

        return properties_dict

    @staticmethod
    def add_event_subscribers(view: ViewABC, control: ControlABC, properties: dict):
        for event_name, subscriber_properties in properties.items():
            event = view.events.find_event(event_name)

            if event:
                subscriber: Optional[Callable] = PropertiesLoader.find_property_method(control, subscriber_properties)

                if not subscriber:
                    raise AttributeError(f"Could not find subscriber for event '{event_name}'")

                event.add_subscriber(subscriber)
                event.add_control(control)
