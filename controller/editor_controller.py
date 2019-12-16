# coding=utf-8
'''
文章编辑接口
'''
from flask import jsonify, Blueprint, request

from service import editor_service

editor_route = Blueprint('editor', __name__,
                         template_folder='templates', url_prefix="/editor")


@editor_route.route('/weight/')
def edit_weight(user_id, article_id, weight):
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
    print(locals())


@editor_route.route('/title/', methods=['GET', 'POST'])
def edit_title(user_id, article_id, title):
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
    data = request.form
    user_id = request.args.get("user_id")
    article_id = request.args.get("article_id")
    title = request.args.get("title")

    print(locals())
    return ''


@editor_route.route('/tags/')
def edit_tags(user_id, article_id, tags):
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
    print(locals())
    return ''
