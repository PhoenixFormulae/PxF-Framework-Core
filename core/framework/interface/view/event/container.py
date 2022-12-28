# System imports
from typing import List, Iterable, MutableSequence

# Local imports
from core.framework.interface.view.event.interfaces import EventABC
from core.framework.interface.view.event import discovery


# External imports


class EventContainer(Iterable):

    def __init__(self, path: MutableSequence[str]):
        self.__event_types: List[type[EventABC]] = discovery.get_events(path)
        self.__events: List[EventABC] = []

    def __iter__(self):
        yield self.__event_types

    def __add__(self, event: type[EventABC]):
        self.add_event(event)

    def __len__(self):
        return len(self.__event_types)

    def find_event_type(self, name: str) -> EventABC | None:
        for event_type in self.__event_types:
            if name.lower() == event_type.kind.lower():
                return event_type

        return None

    def find_event(self, event_name: str) -> EventABC | None:
        for event in self.__events:
            if event.name == event_name:
                return event

        return None

    def add_event(self, event_type: type[EventABC]):
        if event_type not in self.__event_types:
            self.__event_types.append(event_type)

