import logging

def setup_logger(logger_name, log_level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Create a console handler and set its level to the specified log_level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create a formatter and set it to the handler
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger