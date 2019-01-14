from flask import g, request
import json

from app.models import Models
from app.utils import *
from app import auth, serializer, db


class Auth(object):

    def __init__(self, bp):

        @auth.verify_token
        def verify_token(token):
            # g.user = None
            # try:
            #     data = serializer.loads(token)
            # except Exception as e:
            #     return False
            # if 'Account' in data:
            #     g.user = data['Account']
            #     return True
            # return False
            return True

        # GET /login
        # 登录并获取token
        @bp.route('/login', methods=['POST'])
        def get_auth_token():
            data = request.get_json()
            requiredParams = {'Account', 'Password'}
            if data.keys() & requiredParams != requiredParams:
                return make_result(code=Code.NOT_ENOUGH_PARAM)
            else:
                try:
                    user = Models.user.query.filter_by(Account=data['Account'], Password=data['Password']).first()
                    if user is None:
                        return make_result(code=Code.NO_DATA)
                    else:
                        user_agent = request.user_agent
                        status_data = {
                            'ip': request.remote_addr,
                            'msg': user_agent.string,
                            'platform': user_agent.platform,
                            'browser': user_agent.browser,
                            'version': user_agent.version,
                            'content': 'POST /login',
                            'Account': user.Account
                        }
                        status = Models.status(status_data)
                        db.session.add(status)
                        db.session.commit()

                        g.user = user
                        token = g.user.generate_auth_token()
                        result = {
                            'user': user.to_dict(),
                            'token': token.decode('ascii')
                        }
                        return make_result(code=Code.SUCCESS, data=result)
                except:
                    return make_result(code=Code.MYSQL_ERROR)
