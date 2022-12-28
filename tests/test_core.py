# Standard imports
import unittest

# Library imports

# External imports
from core import framework


class CoreExecutionTestCase(unittest.TestCase):

    @staticmethod
    def test_run_core():
        framework.init()


if __name__ == '__main__':
    unittest.main()
