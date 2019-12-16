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
    用户主页
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
    return "user_home"


@user_route.route('/user/setting/')
def setting():
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
    return "setting"


@user_route.route('/user/register/')
def register():
    """
    用户注册
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
            - username
            - password
            - phone
          properties:
            username:
              type: string
              description: 用户名.
            password:
              type: string
              description: 密码.
            phone:
              type: string
              description: phone.

    responses:
      200:
          description: 注册成功
          example: {'code':1,'message':注册成功}
      500:
        description: 注册有误，参数有误等

    """
    return "register"


@user_route.route('/user/login/')
def login():
    """
    用户登录
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
    return "login"
