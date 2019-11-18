# File:           logger.py
# Description:    Wrapper around the logging module
# Author:		    Reinaldo Molina
# Email:          rmolin88 at gmail dot com
# Revision:	    0.0.0
# Created:        Mon Jun 10 2019 17:32
# Last Modified:  Mon Jun 10 2019 17:32

import logging
import os
from logging.handlers import RotatingFileHandler


def set_logger(filename="", size=100, num_backups=5, fmt="", name=""):
    """
    Sets all aspects of the logger
    size is mb
    """

    size *= 1024 * 1024

    if not filename:
        try:
            filename = os.path.splitext(__file__)[0] + ".log"
        except:
            filename = __file__ + ".log"

    if not fmt:
        format = '%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s'
    else:
        format = fmt

    if not name:
        name = __file__

    logger = logging.getLogger(name)
    rhandler = None
    try:
        rhandler = RotatingFileHandler(
            filename, mode='a', maxBytes=size, backupCount=num_backups)
    except:
        raise IOError("Couldn't create/open file \"" + \
                filename + "\". Check permissions.")

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt=format)
    rhandler.setFormatter(formatter)
    logger.addHandler(rhandler)
    return logger


def testaing():
    """docstring for testaing"""

    logger = logging.getLogger(__file__)
    logger.debug("this is another testname.")


if __name__ == '__main__':

    set_logger()
    logger = logging.getLogger(__file__)
    logger.debug("this testname.")
    # Reset logger. Starts a new one
    logger.handlers[0].doRollover()
    # Example of logging an exception
    try:
        testaing()
    except Exception as e:
        logger.error('Failed to open file', exc_info=True)
