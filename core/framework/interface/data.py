# Standard Imports
from dataclasses import dataclass


# Local Imports


# External Imports


@dataclass(slots=True, init=True, order=True)
class BaseWindowConfiguration:
    title: str = 'Phoenix Formulae'
    width: int = 1024
    height: int = 800
    windowed: bool = True
