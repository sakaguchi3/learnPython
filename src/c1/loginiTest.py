# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging.config


# main 処理なので、__name__ には、root が入る

# windowsだとエンコードエラーになる
logging.config.fileConfig('logging.ini')
logger = logging.getLogger('__name__')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


pass
