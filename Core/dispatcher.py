## System Imports
import logging
from abc import ABC


## Application Imports


## Library Imports


class CallDispatcher(ABC):
	
	def __init__(self):
		self.__subscribers: list = []
	
	def __getattr__(self, item) -> list | None:
		found_receivers: list = []
		
		for receiver in self.__subscribers:
			if hasattr(receiver, item):
				found_receivers.append(item)
		
		if len(found_receivers) < 1:
			logging.warning(f"No single receiver found for attribute '{item}' in dispatcher {self.__class__}")
			return None
		
		return found_receivers
	
	def __add__(self, other):
		self.add(other)
	
	def __sub__(self, other):
		self.remove(other)
	
	def add(self, subscriber: object):
		if subscriber not in self.__subscribers:
			self.__subscribers.append(subscriber)
	
	def remove(self, subscriber: object):
		if subscriber in self.__subscribers:
			self.__subscribers.remove(subscriber)
	
	def dispatch(self, name: str, *args):
		for subscriber in self.__subscribers:
			if hasattr(subscriber, name):
				getattr(subscriber, name)(*args)
			
