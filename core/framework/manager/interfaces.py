# Standard imports
from typing import Protocol
from abc import ABC, abstractmethod

# Local imports

# External imports


class Manager(Protocol):
	@classmethod
	def ready(cls):
		...


class ManagerInterface(ABC):
	
	@classmethod
	@abstractmethod
	def ready(cls):
		...

