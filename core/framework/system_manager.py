# System imports

# Local imports

# External imports


class SystemManager(Manager):
	
	@classmethod
	def Ready(cls):
		from core.framework import CoreSystem
		CoreSystem.GameSystem.InitializeInterface()
		
