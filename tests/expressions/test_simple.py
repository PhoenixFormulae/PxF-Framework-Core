# Standard Imports
import unittest

# Local Imports

# External Imports
from pxf_framework_core.framework.expressions import simple


class SimpleExpressionTestCase(unittest.TestCase):
    def test_example_expression(self):

        class SomeClass:
            Prop = 'Hello'

        some_class = SomeClass()

        result = simple.resolve_expression(some_class, '_:Prop:')

        self.assertEqual(result, "Prop")


if __name__ == '__main__':
    unittest.main()
