# Standard Imports
import os
import pkgutil
from importlib import util
from importlib.abc import PathEntryFinder, MetaPathFinder
from typing import MutableSequence, Type

from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
# Local Imports
from pxf_framework_core.framework.system.interfaces import GameSystemABC
from pxf_framework_core.framework.interface.set.discovery import discover_interface_sets_data,\
    discover_interface_sets, import_submodules

# External Imports


def discover_frames_data(system: GameSystemABC, path: str):
    for frame_name in os.listdir(path):

        current_frame = None
        for frame in system.frames:
            if frame_name.lower() == frame.kind.lower():
                current_frame = frame
                break

        if current_frame:
            discover_interface_sets_data(current_frame, f'{path}/{frame_name}/Sets/')


def discover_frames(system: GameSystemABC, path: MutableSequence[str]):

    importer: MetaPathFinder | PathEntryFinder | None
    for importer, name, is_package in pkgutil.iter_modules(path):
        if not is_package:
            continue

        if not importer:
            continue

        current_frame: Type[FrameABC] | None = None
        for frame in system.frames:
            if frame.kind == name:
                current_frame = frame
                break

        if not current_frame:
            continue

        current_frame.control_types.discover_types(current_frame, path)
        current_frame.user_control_types.discover_types(path)

        discover_interface_sets(current_frame, [f'{path[0]}/{name}/'])

        package_spec = importer.find_spec(name)

        if not package_spec:
            continue

        package = util.module_from_spec(package_spec)

        import_submodules(package)
