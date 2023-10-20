import logging

def log_event(event):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info(event)