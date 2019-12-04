import os

VERSION_CODE = 1
VERSION_STRING = '2.0.0'

env = os.environ.get('SERVER_ENV', 'dev-mac')

ROOT_PATH = os.path.abspath('.')
LOG_PATH = ROOT_PATH + '/log/api'

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

MONGO_HOST = "127.0.0.1"
MONGO_USER = "writer"
MONGO_PWD = "writerpwd"
MONGO_PORT = 27017

if __name__ == '__main__':
    pass
