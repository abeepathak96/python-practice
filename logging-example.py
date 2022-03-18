""" 
    Logging library in python provides 5 funtions :- debug(), info(), warning(), error(), critical().
"""

import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('error')
logging.critical('Critical error')