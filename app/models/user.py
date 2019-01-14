from app import db, app, serializer
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from app.utils import md5
from app.code import Code
from datetime import datetime


class tb_user(db.Model):
    account = db.Column(db.String(100), primary_key=True, nullable=False)

    def __init__(self, Account, UserName, Password, UserType='default'):
        self.Account = Account
        self.UserName = UserName
        self.Password = Password
        self.UserType = UserType

    def to_dict(self):
        return sp_user.obj2dict(self)

    @staticmethod
    def obj2dict(o):
        return {
            'Account': o.Account,
            'UserName': o.UserName,
            'UserType': o.UserType,
            'Sex': o.Sex,
            'Birthday': o.Birthday.strftime('%Y-%m-%d %H:%M:%S'),
            'Email': o.Email,
            'MobilePhone': o.MobilePhone,
            'OrganizationCode': o.OrganizationCode,
            'IdentityCard': o.IdentityCard,
            'HeadPortrait': o.HeadPortrait,
            'Score': o.Score,
            'OtherInfo': o.OtherInfo
        }

    @staticmethod
    def list2dict(l):
        return [sp_user.obj2dict(o) for o in l]

    @staticmethod
    def reset():
        users = [
            sp_user(
                Account='20131000669',
                UserName='系统管理员',
                Password=md5('admin'),
                UserType='admin'
            ),
            sp_user(
                Account='20181000001',
                UserName='学生试用账号',
                Password=md5('student'),
                UserType='default'
            )
        ]
        sp_user.query.delete()
        for user in users:
            db.session.add(user)
        db.session.commit()
        return sp_user.list2dict(users)

    def generate_auth_token(self):
        return serializer.dumps({'Account': self.Account})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = sp_user.query.get(data['Account'])
        return user

    @staticmethod
    def query_all():
        l = sp_user.query.all()
        return sp_user.list2dict(l)

    @staticmethod
    def update_data(Account, dictData):
        user = sp_user.query.filter_by(Account=Account)
        if user.first() is None:
            return Code.NO_DATA
        else:
            try:
                if user.update(dictData) > 0:
                    return Code.SUCCESS
                else:
                    return Code.NO_EFFECT
            except:
                return Code.MYSQL_ERROR

    @staticmethod
    def delete_data(Account):
        try:
            if sp_user.query.filter_by(Account=Account).delete() > 0:
                return Code.SUCCESS
            else:
                return Code.NO_EFFECT
        except:
            return Code.MYSQL_ERROR
