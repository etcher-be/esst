# coding=utf-8
"""
Install a handler to redirect all INFO messages (and higher) to the Discord Channel
"""

import logging
import blinker
from esst.core.logger import MAIN_LOGGER


LOGGER = MAIN_LOGGER.getChild(__name__)


class DiscordLoggingHandler(logging.Handler):
    """
    Install a handler to redirect all INFO messages (and higher) to the Discord Channel
    """

    def __init__(self):
        logging.Handler.__init__(self, logging.INFO)

    def emit(self, record: logging.LogRecord):
        """
        Redirects the record to the Discord channel if its level is INFO or higher

        Args:
            record: logging.record to emit
        """
        blinker.signal('discord message').send(__name__, msg=record.msg[:1].upper() + record.msg[1:])


def register_logging_handler():
    """
    Installs the handler to the main logger
    """
    LOGGER.debug('registering Discord logging handler')
    MAIN_LOGGER.addHandler(DiscordLoggingHandler())
