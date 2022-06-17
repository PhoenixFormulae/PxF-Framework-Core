## System Imports
from abc import ABCMeta


## Application Imports
from Core.Interface.View.Control.metaclasses import ControlMeta


## Library Imports


EventMetaInterfaceMixin = type('EventMetaInterfaceMixin', (ABCMeta, ControlMeta), {})

