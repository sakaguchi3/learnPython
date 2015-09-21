# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG, format=formatter)

try:
    v = 3 / 0
    print(v)
except Exception as e:
    logging.error(e)
    print(e)

pass
