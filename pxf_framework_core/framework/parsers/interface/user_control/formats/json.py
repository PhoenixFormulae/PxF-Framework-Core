# System imports
from dataclasses import dataclass, field

# Local imports

# External imports
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True, slots=True, order=True)
class UserControlData:
    name: str
    user_control: str
    control_type: str = field(default='control')
    events: dict = field(default_factory=dict)
    attributes: dict = field(default_factory=dict)
