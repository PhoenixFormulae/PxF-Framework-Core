# Standard Imports
from typing import Callable, List, Dict, Any

from core.framework.interface.view.control.interfaces import ControlABC
# Local Imports
from core.framework.interface.view.event.interfaces import EventABC, EventArgsABC


# Library imports


class BaseEvent(EventABC):
    """
	An event is an action that can be triggered to occur other action occurs,
	for example when the user clicks a button in the mouse, the registered methods will be called.
	"""

    kind: str = "event"

    @property
    def name(self) -> str | None:
        return self.__properties.get('name')

    @name.setter
    def name(self, val: str):
        self.__properties['name'] = val

    @property
    def children(self) -> List[EventABC]:
        return self.__children

    @property
    def controls(self) -> List[ControlABC]:
        return self.__controls

    @property
    def subscribers(self) -> List[Callable]:
        return self.__subscribers

    @property
    def properties(self) -> Dict[str, Any]:
        return self.__properties

    def __init__(self):
        self.__parent: EventABC | None = None

        self.__children: List[EventABC] = []
        self.__controls: List[ControlABC] = []
        self.__subscribers: List[Callable] = []
        self.__properties: Dict[str, Any] = {}

    def set_property(self, name: str, value: object):
        # TODO: Do proper check and resolution of value types
        self.__properties[name] = value

    def add_children(self, events: List):
        for event in events:
            if event not in self.__children:
                self.__children.append(event)
                event.set_parent(self)

    def set_parent(self, parent: EventABC):
        self.__parent = parent

    def add_subscriber(self, subscriber: Callable, recursive: bool = False):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)

        if recursive:
            for event in self.__children:
                event.add_subscriber(subscriber, True)

    def add_control(self, control: ControlABC):
        if control not in self.__controls:
            self.__controls.append(control)

    def bind(self, subscriber: Callable):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)

    def trigger(self, args: EventArgsABC | None = None):
        for subscriber in self.__subscribers:
            if args:
                subscriber(args)
            else:
                subscriber()
