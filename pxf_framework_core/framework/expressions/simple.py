# Standard imports
import re

# Local Imports

# External imports


expression_regex = '_:(.*?):'


def has_expression(expression: str):
    return re.search(expression_regex, expression) is not None


def resolve_expression(target: object, expression: str): # noqa
    match = re.findall(expression_regex, expression)

    if len(match) < 1:
        return expression

    return match[0]
