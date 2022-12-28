# Standard Imports
from typing import List, Type, Iterable, Iterator, MutableSequence

# Local Imports
from core.framework.interface.view.control import discovery
from core.framework.interface.view.control.interfaces import ControlABC
from core.framework.interface.frame.interfaces import FrameABC


# External Imports


# TODO: Since these types containers are similar (user_control, event), perhaps they can be made generic
#       with some abstraction
class ControlContainer(Iterable):
    def __init__(self, path: MutableSequence[str]):
        self.__path = path
        self.__control_types: List[type[ControlABC]] = discovery.get_controls(path)

    def __iter__(self) -> Iterator[Type[ControlABC]]:
        yield self.__control_types

    def __len__(self) -> int:
        raise len(self.__control_types)

    def __add__(self, control_type: Type[ControlABC]):
        if control_type not in self.__control_types:
            self.__control_types.append(control_type)

        return self

    def find_type(self, name: str) -> Type[ControlABC] | None:
        for control_type in self.__control_types:
            if name.lower() == control_type.kind.lower():
                return control_type

        return None

    def discover_types(self, frame: FrameABC, path: MutableSequence[str]):
        pass

    def discover_scripts(self, frame: FrameABC, path: str):
        pass
