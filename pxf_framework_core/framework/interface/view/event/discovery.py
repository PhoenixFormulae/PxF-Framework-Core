# System imports
import sys
import pkgutil
from importlib import util
from typing import List, MutableSequence, Type

# Local imports
from pxf_framework_core.framework.plugins import factory
from pxf_framework_core.framework.interface.view.event.interfaces import EventABC

# External imports


def find_event_types(package_path: MutableSequence[str]) -> List[Type[EventABC]]:
    """
    Searches for all events in a given package module path
    that are registered in the factory

    :param: package_path: The package module path to search in
    :return: The list of event classes
    """

    events: List[Type[EventABC]] = []

    for importer, module_name, is_package in pkgutil.iter_modules(package_path):
        # noinspection DuplicatedCode
        if not is_package:
            continue

        package_spec = importer.find_spec(module_name)

        if not package_spec:
            continue

        package = util.module_from_spec(package_spec)
        sys.modules[module_name] = package
        package_spec.loader.exec_module(package)

        event_names = factory.names_factory(package.__package__)

        for event_name in event_names():
            event_factory = factory.get_factory(package.__package__)

            # TODO: Maybe add type checking to be sure that the class is based of EventInterface
            # just like in the control discovery get_control method does
            event = event_factory(event_name)

            events.append(event)

    return events
