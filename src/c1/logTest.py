# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
'''
import logging


def logtest():
    # setting
    formatter = '%(levelname)s : %(asctime)s : %(message)s'
    logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG, format=formatter)
    # logging
    logging.info('error{}'.format('outputting error'))
    logging.info('warning %s %s' % ('was', 'outputted'))
    logging.info('info %s %s', 'test', 'test')
    logging.warning('warning: {}'.format("message"))


if __name__ == '__main__':
    logtest()
    pass

pass
