# System imports
from abc import ABCMeta

# Local imports
from core.framework.interface.view.control.metaclasses import ControlMeta

# External imports


EventMetaABCMixin = type('EventMetaInterfaceMixin', (ABCMeta, ControlMeta), {})

