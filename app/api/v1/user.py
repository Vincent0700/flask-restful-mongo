from flask import request
from flask_restful import Resource
from app import db
from app.common.utils import make_result
from app.common.code import Code


class User(Resource):
    def get(self, username):
        data = db['user'].find_one(dict(username=username))
        if data:
            return make_result(code=Code.SUCCESS, data=data)
        else:
            return make_result(code=Code.NO_DATA)
