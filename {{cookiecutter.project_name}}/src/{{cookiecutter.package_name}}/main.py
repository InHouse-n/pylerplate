import os

from src import logger_provider


def main():
    """Main function, start coding here"""

    log = logger_provider.get_logger(__name__)
    log.debug("This is a Debug log")
    log.info("This is a information log")
    log.error("This is a Error log")
    log.critical("This is a Critical log")