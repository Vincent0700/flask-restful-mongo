from flask import Flask
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.common.config import cfg
from app.common.utils import register_middleware
from app.middleware.logger import logger
from app.middleware.cors import cors
from app.middleware.nocache import nocache
from app.database.mongodb import MongoDB

app = Flask(__name__)

# Load variables from config.ini
server_host = cfg.get('server.host')
server_port = cfg.getint('server.port')
auth_scheme = cfg.get('auth.scheme')
auth_secret_key = cfg.get('auth.secret_key')
auth_expire = cfg.get('auth.expire')

# Register middleware
register_middleware(app, [
    logger,
    cors,
    nocache
])

# Export modules
logger = app.logger
auth = HTTPTokenAuth(scheme=auth_scheme)
serializer = Serializer(auth_secret_key, expires_in=auth_expire)
mongodb = MongoDB(logger)
db = mongodb.connect()

# Register api
from .api import api_v1_bp

app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
