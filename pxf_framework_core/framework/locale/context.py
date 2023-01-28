# mypy: ignore-errors

# System Imports
import enum
from pathlib import Path

# Local Imports

# External Imports
import hjson  # noinspection PyImport


class LocaleContext:
    def __init__(self):
        pass

    def load_from_path(self, path: Path) -> 'LocaleContext':
        if path.stem == "hjson":
            return self.load_hjson(path)

        raise NotImplementedError(f"Locale file format {path.stem} is not supported")

    @staticmethod
    def load_hjson(path: Path) -> 'LocaleContext':
        contents = path.read_text()
        json = hjson.loads(contents)

        return json


class Output(enum.Enum):
    String = enum.auto()
    Int = enum.auto()

