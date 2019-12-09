#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MongoDBHelper
   Description :
   Author :       sws
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""
from urllib.parse import quote_plus

import pymongo

from common.logger import logger


class MongoDBHelper(object):
    """
        mongoDb
    """

    def __init__(self, host, user, password, db, port=27017):

        self.__uri = "mongodb://%s:%s@%s" % (
            quote_plus(user), quote_plus(password), quote_plus(host))
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
        self.__port = port
        self.__con = None

    def __enter__(self):

        con = pymongo.MongoClient(self.__uri, port=self.__port, maxPoolSize=1)
        self.__con = con
        return con[self.__db]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error("mongoDb occur some error:{} {} {}".format(exc_type, exc_val, exc_tb))

        if self.__con:
            self.__con.close()

        # return True 保证失败不会影响到下一步
        return False


local_mongodb = MongoDBHelper(host="127.0.0.1", user="mongo-admin", password="mongo-password", db="monitor")

if __name__ == '__main__':
    # 测试mongo 插入
    with local_mongodb as condb:
        condb['test'].insert({})
