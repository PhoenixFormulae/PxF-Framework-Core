## System Imports
import sys


## Application Imports
import Core


## Library Imports


sys.path.append(r"python-libs\lib", )
sys.path.append(r"python-libs\DLLs")
sys.path.append(r"python-libs\plugins")


# TODO: Add new Readers/Finders/Loaders/Importers incrementally/dynamically instead of rebuilding meta path
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

if __name__ == '__main__':
    Core.Initialize()
