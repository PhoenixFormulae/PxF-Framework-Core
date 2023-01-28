# Standard Imports
from inspect import signature
from typing import Callable, TYPE_CHECKING

# Local Imports
if TYPE_CHECKING:
    from pxf_framework_core.framework.properties.dispatcher import PropertiesEventDispatcher

# External Imports


class Property:

    @property
    def name(self) -> str | None:
        return self.__name

    def __init__(self, default: object = None):
        self.__default: object = default

        self.__name: str | None = None
        self.__observers: dict[Callable, object] = {}
        self.__value: object = None

    def __set_name__(self, owner: 'PropertiesEventDispatcher', name: str):
        self.__name = name

        from pxf_framework_core.framework.properties.dispatcher import cached_cls_properties
        if owner not in cached_cls_properties:
            cached_cls_properties[owner] = {}

        cached_cls_properties[owner][name] = self

    def __get__(self, instance, owner):
        return self.get()

    def get(self):
        if not self.__value:
            return self.__default

        return self.__value

    def __set__(self, dispatcher: 'PropertiesEventDispatcher', value):
        if self.__value == value:
            return

        old_value = self.__value
        self.__value = value

        event = f'on_{self.__name}'
        if hasattr(dispatcher, event):
            attr = getattr(dispatcher, event)

            if len(signature(attr).parameters) == 1:
                attr(old_value)
            else:
                attr()

        self.dispatch(self.__value)

    def bind(self, observer: Callable, instance: object):
        if observer not in self.__observers:
            self.__observers[observer] = instance

    def dispatch(self, value: object):
        for function, observer in self.__observers.items():
            function(observer, value)


class StringProperty(Property):

    def __init__(self, default: str | None = None):
        super().__init__(default=default)


class IntProperty(Property):

    def __init__(self, default: int | None = None):
        super().__init__(default=default)


class TupleProperty(Property):

    def __init__(self, default: tuple | None = None):
        super().__init__(default=default)


class ListProperty(Property):

    def __init__(self, default: list | None = None):
        super().__init__(default=default)
