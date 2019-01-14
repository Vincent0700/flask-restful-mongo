import hashlib, json, os
from flask import Response
from .code import Code

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def register_middleware(app, middlewares):
    for middleware in middlewares:
        middleware(app)


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def make_result(data=None, code=Code.SUCCESS):
    if data:
        del data['_id']
        
    data = json.dumps({
        'code': code,
        'msg': Code.msg[code],
        'data': data,
    })
    return Response(data, mimetype='application/json')


def md5(s):
    m = hashlib.md5(s.encode('utf-8'))
    return m.hexdigest()
