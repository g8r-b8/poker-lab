from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


class DB:

    def __init__(self):
        self.connection = self.get_db()
        self.db = LocalProxy(self.connection)

    def get_db(self):
        db = getattr(g, "_database", None)
        if self.xonnection is None:
            db = g._database = PyMongo(current_app).db
        return db
