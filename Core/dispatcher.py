## System Imports
import logging


## Application Imports


## Library Imports


class CallDispatcher:
	
	def __init__(self, name: str):
		self.__name = name
		self.__receivers = []
	
	def __getattr__(self, item) -> list | None:
		found_receivers: list = []
		
		for receiver in self.__receivers:
			if hasattr(receiver, item):
				found_receivers.append(item)
		
		if len(found_receivers) < 1:
			logging.warning(f"No single receiver found for attribute '{item}' in dispatcher {self.__name}")
			return None
		
		return found_receivers
		
	def __add__(self, other):
		if other not in self.__receivers:
			self.__receivers.append(other)
	
	def __sub__(self, other):
		if other in self.__receivers:
			self.__receivers.remove(other)
	
