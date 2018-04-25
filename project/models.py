# project/models.py
import datetime
from project import db
from werkzeug import generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    #presence = db.Column(db.ARRAY(WorkDay), nullable=True)

    def __init__(self, email, password, name, admin=False):
        self.email = email
        self.password = generate_password_hash(password)
        self.name = name
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def serialize(self):
        import json

        user_dict = {}
        user_dict['email'] = self.email
        user_dict['name'] = self.name
        return json.dumps(user_dict)

    # UserMixin berisi fungsi ini semua,
    # SEHARUSNYA tanpa definisi dibawah tetap bisa jalan
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)

# Cuma ide, gk yakin jalan
# Tolong dites untuk masuk dan keluar datanya
class Presence(db.Model):
    __tablename__ = "presence"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=True)
    is_present = db.Column(db.Boolean, nullable=False)

    def __init__(self, owner, time=datetime.datetime.now(), is_present=True):
        self.owner = owner
        self.is_present = is_present
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.time = time

    def update_presence(self, is_present):
        self.is_present = is_present
        self.updated_on = datetime.datetime.now()

    def update_time(self, time):
        self.time = time
        self.updated_on = datetime.datetime.now()

    def update_owner(self, owner):
        self.owner = owner
        self.updated_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<WorkDay {0}>'.format(self.id)

# nanti buat jadwal juga
