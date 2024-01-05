import logging
from logging import config
from utils import logfileNamer
from utils.config_parser import parse_config_file
from pathlib import Path


config_path = Path('config.toml')
settings = parse_config_file(config_path)


logroot = "./logs"
logmail_ontvangers = settings.get('email_recipients', [])
loglevel = settings.get('loglevel', 'DEBUG')

filename = logfileNamer(path=logroot, basename="_{{cookiecutter.repo_name}}")


log_config = {
    "version": 1,
    "root": {"handlers": ["console", "file"], "level": loglevel},
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": loglevel,
        },
        "file": {
            "formatter": "std_out",
            "class": "logging.FileHandler",
            "level": loglevel,
            "filename": filename,
        },
    },
    "formatters": {
        "std_out": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - Module: %(module)s - Function: %(funcName)s - Regel: %(lineno)d \nLog : %(message)s",
            "datefmt": "%d-%m-%Y %I:%M:%S",
        }
    },
}
