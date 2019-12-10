# coding=utf-8
'''
用户信息接口
'''
from flasgger import Swagger
from flask import jsonify, app, Blueprint

import os
import config
os.sys.path.append(config.ROOT_PATH)

from model import param
from service.discovery_service import DiscoveryService

discovery_route = Blueprint('discovery', __name__,
                       template_folder='templates')


@discovery_route.route('/discovery/home/')
def discovery_home():
    """
     发现页面主页请求数据
        ---
        tags:
          - 用户信息页面api
        parameters:

        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: 返回默认的文章数据
            schema:
    :return:
    """

    article_list = DiscoveryService.get_article_list()

    param.json_response("", "", article_list)

