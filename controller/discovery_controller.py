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
    用户设置
    ---
    tags:
      - 用户相关接口
    description:
        用户注册接口，json格式
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 用户注册
          required:
            - user_id
          properties:
            user_id:
              type: string
              description: 用户id.
    responses:
      200:
          description: 成功
      500:
        description: 有误等

    """

    article_list = DiscoveryService.get_article_list()

    param.json_response("", "", article_list)

