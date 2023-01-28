# Standard imports
import sys

# Local Imports

# External imports
from pxf_framework_core import framework


def setup_sys_env():
    sys.path.append(r"python-libs\lib", )
    sys.path.append(r"python-libs\DLLs")
    sys.path.append(r"python-libs\plugins")

    # TODO: Add new readers/finders/loaders/Importers incrementally/dynamically instead of rebuilding meta path
    #       Check PEP 302 docs for information on how it works
    """
    sys.meta_path = [
        machinery.BuiltinImporter,
        machinery.FrozenImporter,
        machinery.PathFinder,
        # PackReader,
        # PluginFinder,
        # PackImporter,
        # PluginImporter
    ]
    """


def init():
    setup_sys_env()
    framework.init()


if __name__ == '__main__':
    init()
