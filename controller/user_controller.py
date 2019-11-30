# coding=utf-8
'''
用户信息接口
'''
from flasgger import Swagger
from flask import jsonify, app, Blueprint

user_route = Blueprint('user', __name__,
                       template_folder='templates')


@user_route.route('/user/home/')
def home():
    """
        This is the language awesomeness API 2
        Call this api passing a language name and get back its features
        ---
        tags:
          - Awesomeness Language API
        parameters:
          - name: language2
            in: path
            type: string
            required: true
            description: The language name
          - name: size
            in: query
            type: integer
            description: size of awesomeness
        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: A language with its awesomeness
            schema:
              id: awesome
              properties:
                language:
                  type: string
                  description: The language name
                  default: Lua
                features:
                  type: array
                  description: The awesomeness list
                  items:
                    type: string
                  default: ["perfect", "simple", "lovely"]
        """
    return "home"
    pass


@user_route.route('/user/setting/')
def setting():
    pass
