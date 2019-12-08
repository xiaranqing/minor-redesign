from model.article import Article
from model.param import json_response


class DiscoveryService(object):

    def __init__(self):
        pass

    # todo： 实际的逻辑
    def get_article_list(self):
        article_list = []
        article = Article()

        article_list.append(article)
        return article_list
