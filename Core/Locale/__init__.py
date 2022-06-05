## System Imports


## Application Imports
from Core.Locale.interfaces import LocaleInterface, LocaleContextInterface


## Library Imports


# TODO: This is a temporary mock locale for development, its intention is not defined
class SystemLocale(LocaleInterface):
	
	def GetContext(self, key: str) -> LocaleContextInterface:
		pass


system_locale = SystemLocale()
