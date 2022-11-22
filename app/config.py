import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

env_files = ["config.env"]

config = Config()
for env_file in env_files:
    if os.path.exists(env_file):
        config = Config(env_file)

API_V1_PREFIX = config("API_V1_PREFIX", cast=str)
DEBUG = config("DEBUG", cast=bool)
PROJECT_NAME = config("PROJECT_NAME", cast=str)
VERSION = config("VERSION", cast=str, default="1.0.0")