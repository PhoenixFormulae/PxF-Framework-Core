## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports
from dataclasses_json import dataclass_json


@dataclass(frozen=True, order=True)
class WindowConfiguration:
	
	width: int
	height: int
	x: int
	height: int
	screen: int
	

@dataclass_json
@dataclass(frozen=True, order=True)
class ViewData:
	
	name: str
	controls: dict


