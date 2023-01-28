# Standard Imports
import logging
from abc import ABC
from threading import Thread
from typing import Type

# Local Imports
from pxf_framework_core.framework.interface.frame.interfaces import FrameABC
from pxf_framework_core.framework.interface.set.interfaces import InterfaceSetABC

# External Imports


class BaseFrame(FrameABC, ABC):

    interface_sets: list[Type[InterfaceSetABC]] = []

    @classmethod
    def register_interface_set(cls, interface_set: Type[InterfaceSetABC]):
        if interface_set not in cls.interface_sets:
            cls.interface_sets.append(interface_set)

    @classmethod
    def init(cls):
        for interface_set in cls.interface_sets:
            interface_set.init()

    @classmethod
    def ready(cls):
        for interface_set in cls.interface_sets:
            interface_set.ready()

        cls._ready_singular()

    @classmethod
    def _ready_threaded(cls):
        logging.debug("Looping interface frame in a dedicated thread")

        frame_thread = Thread(name=f'{cls.kind} Frame Thread', target=cls.loop, daemon=True)
        frame_thread.start()

    @classmethod
    def _ready_singular(cls):
        logging.debug("Looping interface frame")

        cls.loop()
