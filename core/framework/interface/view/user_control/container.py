# Standard Imports
from typing import Type, List, Iterable, MutableSequence

# Local Imports
from core.framework.interface.view.user_control.interfaces import UserControlABC
from core.framework.interface.view.user_control.discovery import load_user_control_scripts
from core.framework.interface.view.user_control import discovery


# External Imports


class UserControlContainer(Iterable):

    def __init__(self, path: MutableSequence[str] | None = None, scripts_path: str | None = None):
        self.__path = path
        self.__scripts_path = scripts_path
        self.__user_control_types: List[Type[UserControlABC]] = []

        if self.__path:
            self.discover_types(self.__path)

        if self.__scripts_path:
            self.discover_scripts(self.__scripts_path)

    def __iter__(self):
        yield self.__user_control_types

    def __len__(self) -> int:
        raise len(self.__user_control_types)

    def __add__(self, user_control_type: Type[UserControlABC]):
        if user_control_type not in self.__user_control_types:
            self.__user_control_types.append(user_control_type)

        return self

    def find_type(self, name: str) -> Type[UserControlABC] | None:
        for user_control_type in self.__user_control_types:
            if name.lower() == user_control_type.kind.lower():
                return user_control_type

        return None

    def discover_types(self, path: MutableSequence[str]):
        user_control_types: list[Type[UserControlABC]] = discovery.get_user_controls(path)

        for user_control_type in user_control_types:
            self.__user_control_types.append(user_control_type)

    def discover_scripts(self, path: str):
        user_control_types: list[Type[UserControlABC]] = load_user_control_scripts(path)

        for user_control_type in user_control_types:
            self.__user_control_types.append(user_control_type)
