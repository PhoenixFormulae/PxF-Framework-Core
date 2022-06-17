## System Imports


## Application Imports
from Core.Properties.property import StringProperty
from Core.Properties.dispatcher import PropertiesEventDispatcher


## Library Imports


class TestClass(PropertiesEventDispatcher):
	Hello = StringProperty('There')
	
	def on_Hello(self, *args, **kwargs):
		pass


if __name__ == '__main__':
	test_class = TestClass()
	
	hello = test_class.Hello
	
	test_class.Hello = 'Again'
	
	rep = test_class.Hello.__repr__()
	rp = hello.__repr__()
	
	pass
