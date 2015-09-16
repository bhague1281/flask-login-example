from flask.ext.login import UserMixin
from mongoengine import Document, StringField, connect

class User(Document, UserMixin):
  username = StringField(required=True)
  password = StringField(required=True)

connect('flask_auth_testing')
