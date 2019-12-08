# coding:utf-8
from urllib.parse import urlparse

from pip._vendor import requests

from model.article import Article


class ArticleUpload(object):
    url = ""

    WEIXIN = 0
    TOUTIAO = 1

    WEIXIN_HOSTNAME = 'mp.weixin.qq.com'
    TOUTIAO_HOSTNAME = 'toutiao.com'

    def upload(self):
        pass

    @staticmethod
    def create(article_url, article_content=None):
        if ArticleUpload._get_article_source(article_url) == ArticleUpload.WEIXIN:
            return WeiXinArticleUpload(article_url, article_content)
        elif ArticleUpload._get_article_source(article_url) == ArticleUpload.TOUTIAO:
            return ToutiaoArticleUpload(article_url, article_content)

    @classmethod
    def _get_article_source(self, article_url):
        if article_url.find(self.WEIXIN_HOSTNAME) != -1:
            return self.WEIXIN
        if article_url.find(self.TOUTIAO_HOSTNAME) != -1:
            return self.TOUTIAO


class WeiXinArticleUpload(ArticleUpload):
    pass


class ToutiaoArticleUpload(ArticleUpload):
    TITLE_XPATH = ""
    AUTHOR_XPATH = ""
    CONTENT_XPATH = ""

    def __init__(self, article_url, article_content=None):
        self.article_url = article_url
        self.article_content = ""
        self.article_source = ""
        url_info = urlparse(article_url)
        self.scheme = url_info.scheme  # http or https
        self.netloc = url_info.netloc  # www.jinritouitiao.com
        self.path = url_info.path  # /a123456

    def extract(self):
        article_json = self.__crawler()

        article = Article(article_json)

        self.__storage(article)

        return article

    def __crawler(self):
        # todo: 增加爬虫脚本
        extract_json = dict()
        res = requests.post(self.article_url)

        if (res.status != 200):
            pass

        extract_json["title"] = res.content.xpath(self.TITLE_XPATH)
        extract_json["author"] = res.content.xpath(self.AUTHOR_XPATH)
        extract_json["content"] = res.content.xpath(self.CONTENT_XPATH)

        return extract_json

    def __storage(self, article):


        pass
