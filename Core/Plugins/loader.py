## System Imports
import sys
import pkgutil
import logging
from typing import List
from importlib import util
from inspect import signature


## Application Imports
from Core.Plugins.interfaces import PluginInterface
from Core.Systems.interfaces import GameSystemInterface


## Library Imports
import Plugins


# Package Lookup namespaces for generic plugins
PACKAGE_LOOKUP_NAMESPACES = [
	"Plugins"
]

PLUGINS: List[PluginInterface] = []


def load_all_packages(system: GameSystemInterface):
	for importer, module_name, is_package in pkgutil.iter_modules(Plugins.__path__):
		if is_package:
			load_raw_package(system, importer, module_name)
		else:
			pass
			"""
			files = resources.contents(modname)
			packages = [f[:-PYTHON_PLUGIN_EXTENSION().length()] for f in files if
			            f.endswith(PYTHON_PLUGIN_EXTENSION()) and f[0] != "_"]

			for package in packages:
				print(package)
			"""


def load_raw_package(system: GameSystemInterface, importer, package_name: str):
	# package_module = importer.find_module(package_name).load_module(package_name)
	
	package_spec = importer.find_spec(package_name)
	package = util.module_from_spec(package_spec)
	sys.modules[package_name] = package
	package_spec.loader.exec_module(package)
	
	if not hasattr(package, 'Initialize'):
		raise Exception("Raw plugin package is missing 'Initialize' entrypoint method")
	
	initialize_signature = signature(package.Initialize)
	
	if not issubclass(initialize_signature.return_annotation, PluginInterface):
		raise Exception(f"Raw plugin package 'Initialize' function return type should be '{PluginInterface.__name__}'"
		                f" instead of '{initialize_signature.return_annotation.__name__})'")
	
	plugin_package = package.Initialize()
	
	logger = logging.getLogger('core_logger')
	logger.debug(f"Loaded plugin {package.__alias__} v{package.__version__}")
	
	PLUGINS.append(plugin_package)
	
