# Standard Imports
import logging
import typing

# Local Imports

# External Imports


class CustomFormatter(logging.Formatter):
    grey = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    msg_format: str = "%(asctime)s: [%(levelname)s] %(message)s"

    FORMATS: typing.Dict[int, str] = {
        logging.DEBUG: grey + msg_format + reset,
        logging.INFO: grey + msg_format + reset,
        logging.WARNING: yellow + msg_format + reset,
        logging.ERROR: red + msg_format + reset,
        logging.CRITICAL: bold_red + msg_format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def Initialize():
    # create logger with 'spam_application'
    logger = logging.getLogger("core_logger")
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)

    global core_logger
    core_logger = logging.getLogger('core_logger')


core_logger: logging.Logger
