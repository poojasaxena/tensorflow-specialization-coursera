"""
To setp a basic logger for displaying debug, info, warning & error in code file.
Author: Pooja SAXENA
Datum : 02. Oktober 2021
Place : Hamburg
"""
import logging

def setup_logger(degree,enable=True):
    """
    setup a basic logger with degree=["DEBUG","INFO", "WARNING","ERROR"], 
    could be disable via 'enable' variable, default is enable
    """
    logging.basicConfig(format='%(levelname)s:%(asctime)s: %(message)s',datefmt='%I:%M:%S %p',
                    level=degree)
    logger= logging.getLogger('test-logger')
    logger.disabled=False
    logger.info(f"logger {logger} has Disable::{logger.disabled}")
    return logger

help(setup_logger)
