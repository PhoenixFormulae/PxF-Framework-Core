## framework imports
from abc import ABC


## Application imports
from core.framework import GameSystemInterface


## Library imports


class BaseGameSystem(GameSystemInterface, ABC):
	
	def Ready(self):
		for manager in self.ManagerTypes:
			manager.ready()
		
		self.ReadyPresenters()
		self.InitializeInterface()
	
	def PostReady(self):
		for manager in self.ManagerTypes:
			if hasattr(manager, 'PostReady'):
				manager.PostReady()
		
		self.InitializeInterface()
	
	def ReadyPresenters(self):
		for presenter in self.PresenterTypes:
			presenter.ready()
		
	def InitializeInterface(self):
		for frame in self.Frames:
			frame.ready()

