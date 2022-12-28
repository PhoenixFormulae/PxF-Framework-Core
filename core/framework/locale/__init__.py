# System imports

# Local imports
from core.framework.locale.dispatch import translation_dispatch
from core.framework.locale.context import LocaleContext, Output

# External imports
import i18n


def init():
    i18n.set('filename_format', '{locale}.{format}')
    i18n.set("enable_memoization", True)
    i18n.set('fallback', 'en')


def install() -> bool:
    print("Installing locale context in builtins")
    print("You can now use _LC(/* args */) like a locale_context(LocaleContext).translate(/* args */")

    import builtins
    builtins.__dict__['_LC'] = LC
    builtins.__dict__['_LCI'] = LCI

    return True


# noinspection PyFunctionName
def LC(key: str):
    translation_dispatch(key, output=Output.String)


# noinspection N802
def LCI(key: str):
    translation_dispatch(key, output=Output.Int)

