# /usr/bin/env python
# encoding: utf-8

from common.dbmongo import MongoDBHelper
import config


class MongoService(object):
    """
        mongodb 的增删改查
    """

    def __init__(self):
        self.db = MongoDBHelper(host=config.MONGO_HOST, user=config.MONGO_USER, password=config.MONGO_PWD,
                                port=config.MONGO_PORT)

    def update_data(self, _dic):
        """
        更新的逻辑 先查询
        :param _dic:
        :return:
        """
        pass

    def insert_data(self, _dic):
        """
            插入数据
        :param _dic:
        :return:
        """
        pass

    def select_data(self, _dic):
        """
            查询数据
        :param _dic:
        :return:
        """
        pass
