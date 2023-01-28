# Standard imports
import unittest

# Local imports

# External imports
from pxf_framework_core import framework


class CoreExecutionTestCase(unittest.TestCase):

    @staticmethod
    def test_run_core():
        framework.init()


if __name__ == '__main__':
    unittest.main()
