# Standard Imports
from abc import ABCMeta

# Local Imports


# External Imports


# control Attribute Names
PROPERTY_ATTRIBUTE_NAME = '_property'
EDITABLE_ATTRIBUTE_NAME = '_editable'
REQUIRED_ATTRIBUTE_NAME = '_required'

# control Attribute List Names
PROPERTY_ATTRIBUTE_LIST_NAME = 'properties_functions'
EDITABLE_ATTRIBUTE_LIST_NAME = 'editables_properties'
REQUIRED_ATTRIBUTE_LIST_NAME = 'required_properties'
OPTIONAL_ATTRIBUTE_LIST_NAME = 'optional_properties'


class ControlMeta(type):
    @classmethod
    def __prepare__(metacls, name: str, bases: tuple):  # type: ignore
        return super(ControlMeta, metacls).__prepare__(name, bases)

    def __new__(mcs, name: str, bases: tuple, dct):
        if len(bases) > 0:
            mcs.__determine_property_base(PROPERTY_ATTRIBUTE_NAME, PROPERTY_ATTRIBUTE_LIST_NAME, dct, bases)
            mcs.__determine_required_properties(dct, bases)
            mcs.__determine_property(EDITABLE_ATTRIBUTE_NAME, EDITABLE_ATTRIBUTE_LIST_NAME, dct, bases)

        return super(ControlMeta, mcs).__new__(mcs, name, bases, dct)

    @staticmethod
    def __determine_property_base(attr_name, attr_list_name, dct: dict, bases: tuple):
        if attr_list_name not in dct:
            dct[attr_list_name] = {}

        for base in bases:
            if hasattr(base, attr_list_name):
                base_functions = getattr(base, attr_list_name)
                for attr, val in base_functions.items():
                    dct[attr_list_name][val.property_types_list[0]] = val

        for attr, val in dct.items():
            if hasattr(val, attr_name):
                dct[attr_list_name][val.property_types_list[0]] = val

    @staticmethod
    def __determine_property(attr_name: str, attr_list_name: str, dct: dict, bases: tuple):
        if attr_list_name not in dct:
            dct[attr_list_name] = []

        for base in bases:
            if hasattr(base, attr_list_name):
                for val in getattr(base, attr_list_name):
                    dct[attr_list_name].append(val)

        for attr, val in dct.items():
            if hasattr(val, attr_name):
                for prop in val.property_types_list:
                    dct[attr_list_name].append(prop)

    @staticmethod
    def __determine_required_properties(dct: dict, bases: tuple):
        if REQUIRED_ATTRIBUTE_LIST_NAME not in dct:
            dct[REQUIRED_ATTRIBUTE_LIST_NAME] = []

        for base in bases:
            if hasattr(base, REQUIRED_ATTRIBUTE_LIST_NAME):
                for val in getattr(base, REQUIRED_ATTRIBUTE_LIST_NAME):
                    dct[REQUIRED_ATTRIBUTE_LIST_NAME].append(val)

        if OPTIONAL_ATTRIBUTE_LIST_NAME not in dct:
            dct[OPTIONAL_ATTRIBUTE_LIST_NAME] = []

        for base in bases:
            if hasattr(base, OPTIONAL_ATTRIBUTE_LIST_NAME):
                for val in getattr(base, OPTIONAL_ATTRIBUTE_LIST_NAME):
                    dct[OPTIONAL_ATTRIBUTE_LIST_NAME].append(val)

        for attr, val in dct.items():
            if hasattr(val, REQUIRED_ATTRIBUTE_NAME):
                for prop in val.property_types_list:
                    if getattr(val, REQUIRED_ATTRIBUTE_NAME):
                        dct[REQUIRED_ATTRIBUTE_LIST_NAME].append(prop)
                    else:
                        dct[OPTIONAL_ATTRIBUTE_LIST_NAME].append(prop)


ControlMetaABCMixin = type('ControlMetaInterfaceMixin', (ABCMeta, ControlMeta), {})
