# Standard Imports
import sys
import glob
import pkgutil
from importlib import util
from typing import List, Type, MutableSequence

# Local Imports
from pxf_framework_core.framework.plugins import factory
from pxf_framework_core.framework.interface.view.user_control.interfaces import UserControlABC
from pxf_framework_core.framework.interface.view.user_control.loader import UserControlLoader

# External Imports


def load_user_control_scripts(directory: str):
    user_controls: List[UserControlABC] = []

    for file in glob.glob(f'{directory}/**/*.json', recursive=True):
        user_control: UserControlABC | None = UserControlLoader.load(file)

        if user_control:
            user_controls.append(user_control)

    return user_controls


def find_user_control_types(package_path: MutableSequence[str]) -> List[Type[UserControlABC]]:
    user_controls: List[Type[UserControlABC]] = []

    for importer, module_name, is_package in pkgutil.iter_modules(package_path):
        if not is_package:
            continue

        if not importer:
            continue

        package_spec = importer.find_spec(module_name)
        package = util.module_from_spec(package_spec)
        sys.modules[module_name] = package

        if not package_spec:
            continue

        package_spec.loader.exec_module(package)

        control_names = factory.names_factory(package.__package__)

        for control_name in control_names():
            control_factory = factory.get_factory(package.__package__)

            control = control_factory(control_name)

            if issubclass(control, UserControlABC):
                user_controls.append(control)

    return user_controls
