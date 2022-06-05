## System Imports
from typing import Type


## Application Imports


## Library Imports
from Core.Managers.interfaces import ManagerInterface
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


def register_presenter(interface_set: Type[InterfaceSetInterface]):

	def decorator(cls: Type[PresenterInterface]):
		
		interface_set.RegisterPresenter(cls)
		
		return cls
	
	return decorator
	

def register_manager(manager: Type[ManagerInterface]):
	
	def decorator(cls: Type[PresenterInterface]):
		manager.RegisterPresenter(cls)
		
		return cls
	
	return decorator

