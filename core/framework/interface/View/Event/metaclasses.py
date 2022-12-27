## framework imports
from abc import ABCMeta


## Application imports
from core.framework import ControlMeta


## Library imports


EventMetaInterfaceMixin = type('EventMetaInterfaceMixin', (ABCMeta, ControlMeta), {})

