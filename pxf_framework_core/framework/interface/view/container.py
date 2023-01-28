# Standard Imports
from pathlib import Path
from typing import TypeVar, Generic, Callable, Type, Iterable, Iterator, _T_co

# Local Imports
from pxf_framework_core.framework.interface.view.control.interfaces import ControlABC
from pxf_framework_core.framework.interface.view.event.interfaces import EventABC
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC

# External Imports


C = TypeVar('C', ControlABC, UserControlABC, EventABC)


class Container(Generic[C], Iterable):

    def __init__(self, path: Path, discovery_fn: Callable[[Path], list[Type[C]]]):
        self.__types = discovery_fn(path)

    def __iter__(self) -> Iterator[_T_co]:
        yield self.__types

    def __add__(self, other: Type[C]):
        if other not in self.__types:
            self.__types.append(other)

    def find_type(self, name: str) -> Type[C] | None:
        for c in self.__types:
            if c.name == name:
                return c

