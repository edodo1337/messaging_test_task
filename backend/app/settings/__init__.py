import contextlib

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    a = load_dotenv(find_dotenv())  # load environment variables from .env when using pycharm

from .base import *
from .database import *
from .drf import *
from .cache import *
from .logger import *
from .path import *