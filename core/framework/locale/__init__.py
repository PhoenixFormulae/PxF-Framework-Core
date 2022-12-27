# System imports

# Local imports
from core.framework.locale.interfaces import LocaleInterface, LocaleContextInterface

# External imports


# TODO: This is a temporary mock locale for development, its intention is not defined
class SystemLocale(LocaleInterface):
	
	def GetContext(self, key: str) -> LocaleContextInterface:
		pass


system_locale = SystemLocale()
