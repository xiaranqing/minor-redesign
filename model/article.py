# coding:utf-8


class Article(object):

    def __init__(self):
        pass

    def __init__(self, article_json):
        # 文章标题
        self.title = article_json.get("title","")

        # 文章来源
        self.origin_url = article_json.get("origin_url", "")

        # 文章封面图标
        self.cover_img_url = article_json.get("cover_img_url","")

        # 文章属性标签
        self.tag_list = article_json.get("tag_list","")

        # 文章重要程度0-100
        self.weight = article_json.get("weight")

        # 文章内容
        # todo： 这里content要考虑下存储格式，怎么保留文章格式
        self.content = article_json.get("content")

        # 文章作者列表
        self.author_list = article_json.get("author_list")

        # 发表时间，注意不是数据库中词条的创建时间
        self.publish_time = article_json.get("publish_time")
