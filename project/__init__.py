# project/__init__.py

from flask import Flask

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from project.config import Config
from project import controllers
# config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# routes
@app.route('/')
def index():
    return controllers.index()

@app.route('/signup', methods=['GET', 'POST'])
def register():
    return controllers.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return controllers.login()

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return controllers.logout()
"""
# Request CRUD
# Create
# GET : Show a form to create a new request
@app.route('/request/add', methods=['GET'])
def request_form():
    return controllers.request_form()
# POST : Receive a create request from read (form is in the listing)
@app.route('/request/add', methods=['POST'])
def request_add():
    return controllers.request_add()

# Read
# GET :
# - All : Show list of requests (and create new request right there in the form)
@app.route('/request/all', methods=['POST'])
def request_all():
    return controllers.request_all()

# - Detail : Show a request detail
@app.route('/request/<request_id>', methods=['GET'])
def request_detail(request_id):
    return controllers.request_detail(request_id)

# Update
# POST : Change the details of the request made (i.e. Change)
@app.route('/request/<request_id>', methods=['POST'])
def request_update(request_id):
    return controllers.request_update(request_id)

# Delete
# POST : Delete a request
@app.route('/request/<request_id>', methods=['DELETE'])
def request_delete(request_id):
    return controllers.request_delete(request_id)

# API CRUD
# Create
# Receive a create request from read (form is in the listing)
@app.route('/api/request/add', methods=['GET', 'POST'])
def request_add():
    return controllers.request_add()

# Read
# GET :
# - All : Show list of requests (and create new request right there in the form)
@app.route('/api/request/all', methods=['POST'])
def api_request_all():
    return controllers.api_request_all()

# - Detail : Show a request detail
@app.route('/api/request/<request_id>', methods=['GET'])
def api_request_detail(request_id):
    return controllers.api_request_detail(request_id)

# Update
# POST : Change the details of the request made (i.e. Change)
@app.route('/api/request/<request_id>', methods=['POST'])
def api_request_update(request_id):
    return controllers.api_request_update(request_id)

# Delete
# POST : Delete a request
@app.route('/api/request/<request_id>', methods=['DELETE'])
def api_request_delete(request_id):
    return controllers.api_request_delete(request_id)

"""