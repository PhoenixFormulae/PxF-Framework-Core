## framework imports
from dataclasses import dataclass


## Application imports


## Library imports


@dataclass(slots=True, init=True, order=True)
class BaseWindowConfiguration:

	title: str = 'Phoenix Formulae'
	width: int = 1024
	height: int = 800
	windowed: bool = True

