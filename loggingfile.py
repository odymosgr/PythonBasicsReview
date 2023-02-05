import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug('Debug messagge')
# logging.info('Info message')
# logging.warning('Warning message')
# logging.error('Error message')
# logging.critical('Critical message')

import helperlogger




logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.debug('Debug messagge')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')

# also a file can be used: logging.conf

import traceback
try:
  a = [1,2,3]
  val = a[4]
except:
  logging.error(f'The error is {traceback.format_exc()}')


# see also
# from logging.handlers import RotatingFileHandler
# from logging.handlers import TimedRotatingFileHandler
