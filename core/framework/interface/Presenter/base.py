## framework imports
from abc import ABC
from typing import Type


## Application imports


## Library imports
from core.framework import ViewInterface
from core.framework import PresenterInterface


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
		
