## framework imports
from abc import ABC
from typing import Type


## Application imports
from core.framework import InterfaceSetInterface
from core.framework import PresenterInterface
from core.framework import UserControlContainer


## Library imports


class BaseInterfaceSet(InterfaceSetInterface, ABC):
	
	@classmethod
	def Ready(cls):
		pass

		
