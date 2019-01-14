from pymongo import MongoClient
from app.common.config import cfg
from app.common.utils import md5


class MongoDB:
    def __init__(self, logger):
        self.host = cfg.get('mongodb.host')
        self.port = cfg.getint('mongodb.port')
        self.database = cfg.get('mongodb.database')
        self.require_authentication = cfg.getboolean('mongodb.require_authentication')
        if self.require_authentication:
            self.username = cfg.get('mongodb.username')
            self.password = cfg.get('mongodb.password')
            self.auth_db = cfg.get('mongodb.auth_db')

        self.logger = logger
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(f'{self.host}:{self.port}')
        if self.require_authentication:
            self.client[self.auth_db].authenticate(self.username, self.password)
        self.db = self.client[self.database]
        self.initialize()
        return self.db

    def initialize(self):
        cols = self.db.collection_names()
        if 'user' not in cols:
            user = dict(
                username='admin',
                password=md5('admin')
            )
            self.db["user"].insert_one(user)
