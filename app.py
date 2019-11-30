import random

from flask import Flask, jsonify
from flasgger import Swagger
from pip._vendor.urllib3 import request

import config
from controller import user_controller

app = Flask(__name__)
app.register_blueprint(user_controller.user_route)

app.config.from_object(config)

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = ""    # 配置大标题
swagger_config['description'] = ""    # 配置公共描述内容
swagger_config['host'] = ""    # 请求域名

Swagger(app, config=swagger_config)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/<string:language>/', methods=['GET'])
def index(language):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - Awesomeness Language API
    parameters:
      - name: language
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

    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


if __name__ == '__main__':
    app.run()
