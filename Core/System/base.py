## System Imports
from abc import ABC


## Application Imports
from Core.System.interfaces import GameSystemInterface


## Library Imports


class BaseGameSystem(GameSystemInterface, ABC):
	
	def Ready(self):
		for manager in self.ManagerTypes:
			manager.Ready()
		
		self.ReadyPresenters()
		self.InitializeInterface()
	
	def PostReady(self):
		for manager in self.ManagerTypes:
			if hasattr(manager, 'PostReady'):
				manager.PostReady()
		
		self.InitializeInterface()
	
	def ReadyPresenters(self):
		for presenter in self.PresenterTypes:
			presenter.Ready()
		
	def InitializeInterface(self):
		for frame in self.Frames:
			frame.Ready()

