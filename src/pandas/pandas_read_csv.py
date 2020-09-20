# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config as lg
from logging import DEBUG

import pandas as pd
from numpy import ndarray
from pandas.core.series import Series


def log_init():
    # setting
    formatter = '%(levelname)s : %(asctime)s : %(message)s'
    lg.basicConfig(filename='logfile/logger.log', level=DEBUG, format=formatter)


cnt: Series = pd.Series([10, 20, 30, 50, 80, 130])
v2: ndarray = cnt.values


def csvload():
    pass


if __name__ == '__main__':
    log_init()
    print('start')
    pass

pass

if __name__ == '__main__':
    log_init()
    print('start')
    pass

pass
