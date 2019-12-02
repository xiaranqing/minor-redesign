#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     logger
   Description :
   Author :       sws
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

import logging.config

# 配置日志
FORMAT = "%(asctime)-15s %(threadName)s %(filename)s:%(lineno)d %(levelname)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger('crawlLog')
logger.setLevel(logging.NOTSET)
