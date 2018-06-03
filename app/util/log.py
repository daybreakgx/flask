import logging
import logging.config

logging.config.fileConfig("logging_app.ini")
logger = logging.getLogger('app')
