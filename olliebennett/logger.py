"""
Custom Logging facility.
"""

import logging
from time import gmtime, strftime
import os
import olliebennett.config.logger as LogConfig

__author__ = 'Ollie Bennett | http://olliebennett.co.uk/'

# Available Log Types
TWITTER = "Twitter"
TEMPERATURE = "Temperature"

# Create loggers (for later use).
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-5s %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
# Twitter:
twitter_log = logging.getLogger(TWITTER)
twitter_log.setLevel(logging.DEBUG)
twitter_fh = logging.FileHandler(LogConfig.LOG_PATH_TWITTER)
twitter_fh.setFormatter(formatter)  # add formatter to file handler
twitter_log.addHandler(twitter_fh)  # add file handler to logger
# Temperature:
temperature_log = logging.getLogger(TEMPERATURE)
temperature_log.setLevel(logging.DEBUG)
temperature_fh = logging.FileHandler(LogConfig.LOG_PATH_TEMPERATURE)
temperature_fh.setFormatter(formatter)  # add formatter to file handler
temperature_log.addHandler(temperature_fh)  # add file handler to logger


def debug(log_type, log_message):
    logging.getLogger(log_type).debug(log_message)


def info(log_type, log_message):
    logging.getLogger(log_type).info(log_message)


def warn(log_type, log_message):
    logging.getLogger(log_type).warn(log_message)


def error(log_type, log_message):
    logging.getLogger(log_type).error(log_message)
