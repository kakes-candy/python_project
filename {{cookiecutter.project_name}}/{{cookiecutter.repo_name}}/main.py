from pathlib import Path
from config.logging_config import create_logger


# -------------------------------------------------------------------------------------------------------
# LOGGING Initialiseren
# -------------------------------------------------------------------------------------------------------

logconfigfile = Path('config.toml')
rootlogger = create_logger(logconfigfile)
rootlogger.info("logger initialised")
