## System Imports
import re

## Application Imports


## Library Imports


expression_regex = '_:(.*?):'


def has_expression(expression: str):
	return re.search(expression_regex, expression) is not None


def resolve_expression(target: object, expression: str):
	match = re.findall(expression_regex, expression)
	
	if len(match) < 1:
		return expression
	
	return match[0]

	
class SomeClass:
	
	Prop = 'Hello'


if __name__ == '__main__':

	some_class = SomeClass()
	
	result = resolve_expression(some_class, '_:Prop:')
	
	pass

