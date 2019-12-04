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
    print(locals())


@editor_route.route('/title/', methods=['GET', 'POST'])
def edit_title():
    data = request.form
    user_id = request.args.get("user_id")
    article_id = request.args.get("article_id")
    title = request.args.get("title")

    print(locals())
    return ''


@editor_route.route('/content/')
def edit_content(user_id, article_id, title):
    print(locals())
    return ''


@editor_route.route('/tags/')
def edit_tags(user_id, article_id, tags):
    print(locals())
    return ''
