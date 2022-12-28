# Standard imports
import typing
from typing import Dict, Optional, List, Any, TYPE_CHECKING

# Library imports
from core.framework.interface.view.event.interfaces import EventABC
from core.framework.interface.view.control.metaclasses import PROPERTY_ATTRIBUTE_LIST_NAME

if TYPE_CHECKING:
    from core.framework.interface.frame.interfaces import FrameABC


# External imports


class EventLoader:

    def __init__(self, frame: 'FrameABC'):
        self.__frame: FrameABC = frame
        self.__indent: int = 1

    def load_events(self, properties: Dict) -> List[EventABC]:
        events: List[EventABC] = []

        for name, properties in properties.items():
            event_properties = properties
            event_properties['name'] = name

            event = self.load_event(event_properties)
            if event:
                events.append(event)

        return events

    def load_event(self, properties: Dict) -> EventABC | None:
        if 'type' not in properties:
            return None

        event_type: Optional[type[EventABC]] = self.__frame.event_types.find_type(properties['type'])

        if not event_type:
            raise ModuleNotFoundError(f"Could not find event with type {properties['type']}")

        event = event_type()
        self.load_event_properties(event, properties)

        return event

    def load_event_properties(self, event: EventABC, properties: dict):
        self.__check_properties_requirements(event, properties)

        event.name = properties['name']

        print("".ljust(2 * self.__indent) + f"{event.name} ({type(event).__name__}/{event.kind})")

        for key, val in properties.items():
            print("".ljust(2 * self.__indent) + f"- {key}")

        properties_list = {}
        cur_cls = event

        while True:
            properties = getattr(cur_cls, PROPERTY_ATTRIBUTE_LIST_NAME)
            for key, val in properties.items():
                if key not in properties_list:
                    properties_list[key] = val

            if not hasattr(cur_cls.parent_cls, "parent_cls"):
                break

            cur_cls = cur_cls.parent_cls

        for key, val in properties_list.items():
            self.__load_event_property(event, key, properties)

        if 'children' in properties:
            print("".ljust(2 * self.__indent) + f"children:")
            self.__indent += 1

            event.add_children(self.__load_children(properties['children']))

    def __load_children(self, children: Dict) -> List[EventABC]:
        events: List[EventABC] = []

        for child in children.items():
            child_properties: Dict = child[1]
            child_properties["name"] = child[0]

            event: Optional[EventABC] = self.load_event(child_properties)

            if event:
                events.append(event)

        return events

    def __load_event_property(self, event: EventABC, prop_key: Any, event_properties: Dict):
        properties_list: typing.Dict[str, typing.Callable] = {}
        mandatory_properties: typing.List[str] = []
        optional_properties: typing.List[str] = []

        # Check all property keys
        prop_keys = ()

        if type(prop_key) == str:
            prop_keys += (prop_key,)

        elif type(prop_key) == tuple:
            for prop in prop_key:
                prop_keys += (prop,)

        else:
            raise Exception(f"Property key should be 'str' or 'tuple' got '{type(prop_key)}' instead.")

        # Check if the necessary property values are present
        for properties_key in prop_keys:
            if properties_key in optional_properties and \
                    properties_key not in mandatory_properties and \
                    properties_key not in event_properties:
                print("".ljust(4 * self.__indent) + f"Skipping optional property: {properties_key}")
                return

        # Get each control property values
        args = (event,)
        for prop in prop_keys:
            prop_val = event_properties[prop]

            args += (prop_val,)

        if len(args) > 1:
            properties_list[prop_key](*args)

    def __check_properties_requirements(self, event: EventABC, event_properties: Dict):
        # Check if there is missing properties in the view script model
        missing_mandatory_properties = self.__check_mandatory_properties(event, event_properties)

        # Raise an exception if there is any missing mandatory property in the list
        if len(missing_mandatory_properties) > 0:
            raise IncompleteEventPropertiesException(event, missing_mandatory_properties)

    @staticmethod
    def __check_mandatory_properties(event: EventABC, event_properties: Dict) -> List[str]:
        # Check if all the mandatory properties are present in view Script properties
        missing_property_list = []

        mandatory_attribute_list = getattr(event, MANDATORY_ATTRIBUTE_LIST_NAME)

        for mandatory_property in mandatory_attribute_list:
            if type(mandatory_property) == str:
                if mandatory_property not in event_properties:
                    missing_property_list.append(mandatory_property)

            elif type(mandatory_property) == tuple:
                for combined_property in mandatory_property:
                    if combined_property not in event_properties:
                        missing_property_list.append(combined_property)

            else:
                raise Exception(f"Property should be 'string' or 'tuple', got {type(mandatory_property)} instead.")

        return missing_property_list
