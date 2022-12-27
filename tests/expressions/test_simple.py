# Standard Imports
import unittest

# Local Imports
from core.framework.expressions import simple

# External Imports


class SimpleExpressionTestCase(unittest.TestCase):
    def test_example_expression(self):

        class SomeClass:
            Prop = 'Hello'

        some_class = SomeClass()

        result = simple.resolve_expression(some_class, '_:Prop:')

        self.assertEqual(result, "World")


if __name__ == '__main__':
    unittest.main()
