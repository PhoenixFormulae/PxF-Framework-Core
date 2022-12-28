# Standard imports
import unittest

# Library imports

# External imports
from core.framework.parsers.interface.user_control.formats import json


user_control_input_json = """
{
    "name": "test",
    "user_control": "test",
    "control_type": "control",
    "events": {},
    "attributes": {}
}
"""


class UserControlJSONTestCase(unittest.TestCase):

    def test_parse_json(self):
        user_control_data = json.UserControlData.from_json(user_control_input_json)

        expected_result = json.UserControlData(
            name="test",
            user_control="test",
            events={},
            attributes={}
        )

        self.assertEqual(expected_result, user_control_data)


if __name__ == '__main__':
    unittest.main()
