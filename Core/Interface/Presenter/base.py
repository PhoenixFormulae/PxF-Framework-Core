## System Imports
from abc import ABC
from typing import Type


## Application Imports


## Library Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


class BasePresenter(PresenterInterface, ABC):
	
	_protocol = None
	
	@classmethod
	def RegisterView(cls, view: Type[ViewInterface]):
		if view not in cls.Views:
			cls.ViewTypes.append(view)

	@classmethod
	def Ready(cls):
		for view_type in cls.ViewTypes:
			cls.Views.append(view_type())
		
