# coding=utf-8

"""
上传数据源
"""

from flask import jsonify, app, Blueprint

from service.upload_service import ArticleUpload

upload_route = Blueprint('upload', __name__,
                         template_folder='templates')


@upload_route.route('/upload/')
def upload_from_url(url):
    """
     从url中获取数据源
        ---
        tags:
          - 上传文章api
        parameters:
          - name: url
            in: path
            type: string
            required: true
            description: 数据源api

        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: 返回默认的文章数据
            schema:
    :return:
    """
    article = ArticleUpload.create(url).extract()
    pass
