# System imports
import logging

# Local imports
from core.framework.plugins import loader


# External imports


def init():
    logging.info("Loading plugin packages")
    loader.load_all_packages()
