import logging
from config.logging_config import log_config


# -------------------------------------------------------------------------------------------------------
# LOGGING Initialiseren
# -------------------------------------------------------------------------------------------------------
logging.config.dictConfig(log_config)
rootlogger = logging.getLogger()
rootlogger.setLevel(logging.DEBUG)
log_filename = log_config.get('handlers').get('file').get('filename')

rootlogger.info(f"logger initialised, logfilename: {log_filename}")
