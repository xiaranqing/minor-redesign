
import os

VERSION_CODE = 1
VERSION_STRING = '2.0.0'

env = os.environ.get('SERVER_ENV', 'dev-mac')

ROOT_PATH = os.path.abspath('.')
LOG_PATH = ROOT_PATH + '/log/api'

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


if __name__ == '__main__':
    pass

