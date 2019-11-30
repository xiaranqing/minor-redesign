# coding=utf-8
'''
用户信息接口
'''
from flasgger import Swagger
from flask import jsonify, app, Blueprint

user_route = Blueprint('user', __name__,
                       template_folder='templates')


@user_route.route('/user/home/')
def user_home(user_id):
    """
        用户信息页面
        ---
        tags:
          - 用户信息页面api
        parameters:
          - name: user_id
            in: query
            type: String
            description: 用户Id
        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: 返回页面
            schema:
              id: 123
              properties:
                mesasge:
                  type: string
                  description: yyy
                  default: xxx
        """
    return "user_home"


@user_route.route('/user/setting/')
def setting():
    return "setting"


@user_route.route('/user/register/')
def register():
    return "register"


@user_route.route('/user/login/')
def login():
    return "login"
