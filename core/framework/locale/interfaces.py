## framework imports
from abc import ABC, abstractmethod


## Application imports


## Library imports


class LocaleContextInterface(ABC):
	
	@abstractmethod
	def String(self, key: str):
		pass
	
	@abstractmethod
	def Int(self, key: str):
		pass


class LocaleInterface(ABC):
	
	@abstractmethod
	def GetContext(self, key: str) -> LocaleContextInterface:
		pass

