## System Imports
from typing import Type


## Application Imports


## Library Imports
from Core.Interface.View.interfaces import ViewInterface
from Core.Interface.Presenter.interfaces import PresenterInterface


class BasePresenter(PresenterInterface):
	
	ViewTypes: list[Type[ViewInterface]] = []
	Views: list[ViewInterface] = []
	
	@classmethod
	def RegisterView(cls, view: Type[ViewInterface]):
		if view not in cls.Views:
			cls.ViewTypes.append(view)

	@classmethod
	def Ready(cls):
		for view_type in cls.ViewTypes:
			cls.Views.append(view_type())
		
