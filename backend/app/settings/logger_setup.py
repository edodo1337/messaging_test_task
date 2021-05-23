from django.conf import settings
import logging.config
import os
import logging
import logging.handlers


def configure_logger(name=None):
    conf = settings.BASE_LOGGER_CONFIG

    logging.config.dictConfig(conf)
    logger = logging.getLogger(name)
    return logger

