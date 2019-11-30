# coding=utf-8
'''
文章编辑接口
'''
from flask import jsonify, Blueprint

from service import editor_service

editor_route = Blueprint('discovery', __name__,
                         template_folder='templates')


@editor_route.route('/editor/tag/')
def edit_tag(article_id, tag_list):
    article = editor_service.find(article_id)
    article.tag_list = tag_list
    editor_service.update(article)


@editor_route.route('/editor/weight/')
def edit_weight(article_id, weight):
    article = editor_service.find(article_id)
    article.weight = weight
    editor_service.update(article)

