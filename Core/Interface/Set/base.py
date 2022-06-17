## System Imports
from abc import ABC
from typing import Type


## Application Imports
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.Presenter.interfaces import PresenterInterface
from Core.Interface.View.UserControl.container import UserControlContainer


## Library Imports


class BaseInterfaceSet(InterfaceSetInterface, ABC):
	
	@classmethod
	def Ready(cls):
		pass

		
