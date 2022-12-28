# Standard imports
import importlib
import os
import sys
import pkgutil
from importlib import util
from typing import MutableSequence

# Local imports
from core.framework.interface.frame.interfaces import FrameABC


# External imports


def discover_interface_sets_data(frame: FrameABC, path: str):
    for interface_set_name in os.listdir(path):
        user_controls_directory = f'{path}/{interface_set_name}/UserControls/'

        current_interface_set = None
        for interface_set in frame.interface_sets:
            if interface_set_name.lower() == interface_set.name.lower():
                current_interface_set = interface_set
                break

        if current_interface_set:
            current_interface_set.user_control_types.discover_scripts(user_controls_directory)


def import_submodules(package, recursive=True):
    if isinstance(package, str):
        package = importlib.import_module(package)

    results = {}

    for loader, name, is_pkg in pkgutil.iter_modules(package.__path__):
        full_name = package.__package__ + '.' + name

        if not is_pkg:
            module = importlib.import_module(full_name)
            results[full_name] = module

        if recursive and is_pkg:
            results.update(import_submodules(full_name))

    return results


# noinspection PyUnusedLocal
def discover_interface_sets(frame: FrameABC, path: MutableSequence[str]):
    for importer, name, is_package in pkgutil.iter_modules(path):
        if not is_package:
            continue

        spec = importer.find_spec(name)

        if not spec:
            continue

        package = util.module_from_spec(spec)
        sys.modules[name] = package
        spec.loader.exec_module(package)

        for set_importer, set_name, is_set_package in pkgutil.iter_modules(package.__path__):
            if not is_set_package:
                continue

            current_interface_set = None
            for interface_set in frame.interface_sets:
                if set_name.lower() == interface_set.name.lower():
                    current_interface_set = interface_set

        # if current_interface_set:
        # 	current_interface_set.UserControlTypes.DiscoverScripts(package.__path__[0])
