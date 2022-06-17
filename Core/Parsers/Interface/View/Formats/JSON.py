## System Imports
from dataclasses import dataclass, field


## Application Imports


## Library Imports
from dataclasses_json import dataclass_json


@dataclass(frozen=True, slots=True, order=True)
class WindowConfiguration:
	
	width: int
	height: int
	x: int
	height: int
	screen: int


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



