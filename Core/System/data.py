## System Imports
from dataclasses import dataclass, field


# Application Imports


# Library Imports
from dataclasses_json import dataclass_json


@dataclass(frozen=True, slots=True, order=True)
class GameSystemDetails:
	
	logo_path: str


@dataclass_json
@dataclass(frozen=True, slots=True, order=True)
class GameSystemConfiguration:
	
	name: str
	details: GameSystemDetails

