# coding:utf-8
from urllib.parse import urlparse
from lxml import etree

import requests
from model.article import Article


class ArticleUpload(object):
    request_headers = {
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

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
    TOUTIAO_XPATH = {"article_body_path": "//div[@id='article-main']",
                     "article_title_path": ".//h1[@class='article-title']/text()"}

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
        res = requests.post(self.article_url, headers=self.request_headers, verify=False)

        if (res.status_code != 200):
            print(">>>>res error")
            return ""

        html = res.text

        html_etree = etree.HTML(html)
        extract_json["title"] = html_etree.xpath(self.TOUTIAO_XPATH["article_title_path"])
        extract_json["content"] = html_etree.xpath(self.TOUTIAO_XPATH["article_body_text_path"])

        return extract_json

    def __storage(self, article):
        pass


if __name__ == "__main__":
    url = u"https://www.toutiao.com/a6769444526911128068/"

    # todo: 头条升级了爬虫，已经抓不到了。
    a = ArticleUpload.create(url).extract()
    print(">>>a:", a)
