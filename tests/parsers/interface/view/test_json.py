# Standard imports
import unittest

# Local Imports
from pxf_framework_core.framework.parsers.interface.view.formats import json

# External imports


view_input_json = """
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


class ViewJSONTestCase(unittest.TestCase):

    def test_parse_json(self):
        view_data = json.ViewData.from_json(view_input_json)

        expected_result = json.ViewData(
            name="test",
            x=10, y=20,
            width=200, height=200,
            children={},
            events={}
        )

        self.assertEqual(expected_result, view_data)


if __name__ == '__main__':
    unittest.main()
