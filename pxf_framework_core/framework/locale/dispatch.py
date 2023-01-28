# mypy: ignore-errors

# System Imports

# Local Imports
from pxf_framework_core.framework.locale.context import Output

# External Imports
# noinspection PyPackageRequirements
import i18n


def translation_dispatch(key: str, output: Output) -> str | None: # noqa
    value = i18n.t(key)

    return value
