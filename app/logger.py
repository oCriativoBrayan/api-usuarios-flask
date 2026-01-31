import logging
from logging.handlers import RotatingFileHandler    

def setup_logger():
    logger = logging.getLogger('api')
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler('app/logs/app.log', maxBytes=5_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger