# System imports
from dataclasses import dataclass, field

# Local imports

# External imports
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True, slots=True, order=True)
class ViewData:
    name: str
    x: int
    y: int
    width: int
    height: int
    children: dict
    events: dict = field(default_factory=dict)
