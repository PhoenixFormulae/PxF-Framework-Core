## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports


@dataclass(frozen=True, order=True)
class BaseWindowConfiguration:

	title: str = 'Phoenix Formulae'
	width: int = 800
	height: int = 600
	windowed: bool = True

