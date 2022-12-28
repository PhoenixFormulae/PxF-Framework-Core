# mypy: ignore-errors

# System Imports

# Local Imports
from core.framework.locale.context import Output

# External Imports
import i18n


def translation_dispatch(key: str, output: Output) -> str | None: # noqa
    value = i18n.t(key)

    return value
