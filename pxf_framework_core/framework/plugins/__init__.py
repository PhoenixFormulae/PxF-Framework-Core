# System imports
import logging

# Local imports
from pxf_framework_core.framework.plugins import loader

# External imports


def init():
    logging.info("Loading plugin packages")
    loader.load_all_packages()
