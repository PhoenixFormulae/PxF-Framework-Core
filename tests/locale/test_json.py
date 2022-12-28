# Standard imports
import unittest

from core.framework import locale

# Library imports

# External imports


locale_input_json = """
{
    "name": "test",
    "x": 10, "y": 20,
    "width": 200, "height": 200,
    "user_control": "test",
    "control_type": "control",
    "events": {},
    "attributes": {},
    "children": {}
}
"""


class LocaleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        from core.framework import locale
        locale.init()
        locale.install()

    def test_locale_load(self):
        self.fail()

    def test_locale_en_translate(self):
        self.assertEqual("Foo", locale.LCI("FOO"))


if __name__ == '__main__':
    unittest.main()
