import os
from .path import BASE_DIR

DEBUG = bool(os.getenv('DEBUG'))

BASE_LOG_PATH = os.path.join(BASE_DIR, 'logs')


BASE_LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        # 'django': {
        #     'level': 'DEBUG' if DEBUG else 'INFO',
        #     'handlers': ['console', 'file']
        # },
        'messaging': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['console', 'file']
        },
    }
}

MESSAGES_FILE_PATH = 'messages'
