from flask import Blueprint
from flask_restful import Api

api_v1_bp = Blueprint('v1', __name__)
api = Api(api_v1_bp)

from .user import User

api.add_resource(User, '/user/<string:username>')
