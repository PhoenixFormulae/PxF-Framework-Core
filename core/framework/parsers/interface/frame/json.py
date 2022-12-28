# System imports
from dataclasses import dataclass

# Local imports

# External imports


@dataclass(frozen=True, slots=True, order=True)
class WindowConfiguration:
    width: int
    height: int
    x: int
    # y: int
    screen: int
