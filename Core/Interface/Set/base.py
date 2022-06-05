## System Imports
from abc import ABC
from typing import Type


## Application Imports


## Library Imports
from Core.Interface.Set.interfaces import InterfaceSetInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


class BaseInterfaceSet(InterfaceSetInterface, ABC):
	
	PresenterTypes: list[Type[PresenterInterface]] = []
	
	def __init__(self):
		self._presenters: list[PresenterInterface] = []
	
	@classmethod
	def RegisterPresenter(cls, presenter_type: Type[PresenterInterface]):
		if presenter_type not in cls.PresenterTypes:
			cls.PresenterTypes.append(presenter_type)
	
	def Ready(self):
		for presenter_type in self.PresenterTypes:
			presenter_type.Ready()
		
