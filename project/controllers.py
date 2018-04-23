#project/controllers.py
from flask import flash, render_template, request, session

def index():
    if session.get('logged_in'):
        return render_template('dashboard.html')
    else:
        return render_template('login.html')

def login():
    # if login is being done
    if request.method=='POST':
        # check login credentials
        from project.models import User
        from project import bcrypt

        if request.form['email'] != None and request.form['password'] != None:
            print(request.form['email'])
            print(request.form['password'])

            user = User.query.filter_by(email=request.form['email']).first()
            password = request.form['password'].encode("utf-8")

            if user and bcrypt.check_password_hash(user.password.encode("utf-8"), password):
                print("Logged in!")
                session['logged_in']=True
            else:
                print("Log in credentials are false")
        else:
            print("Please fill in the email and password!")

    # if login page iss fetched
    elif request.method=='GET':
        # Login page is fetched
        print("Login page is fetched usign GET directly!")
        #return index()
    return index()

def register():
    # if login is being done
    if request.method=='POST':
        if request.form['email'] != None:

            if request.form['password']!=None and request.form['name']!=None:
                from project.models import User
                from project import db

                email = request.form['email']
                password = request.form['password']
                name = request.form['name']

                user = User(email=email, password=password, name=name, admin=True)
                try:
                    db.session.add(user)
                    db.session.commit()
                    status = 'success'
                except Exception as e:
                    print("Error : " + str(e))
                    status = 'this user is already registered'
                print(status)
                db.session.close()
            else:
                return flash('please fill in all the creds')
        else:
            return flash('please fill in the email!')
    elif request.method=='GET':
        print("Signup page is fetched using GET directly!")
        return render_template('signup.html')
    return index()

def logout():
    session.pop('logged_in', None)
    return index()

# IoT related methods
"""
def open_req_create():
    print("Entered Create")
    return flash("Not yet implemented")

def open_req_read(id):
    print("Entered Read. Id : " + id)
    return flash("Not yet implemented")

def open_req_update(id):
    print("Entered Update. Id : " + id)
    return flash("Not yet implemented")

def open_req_delete(id):
    print("Entered Delete. Id : " + id)
    return flash("Not yet implemented")
"""
# API crud
"""
def api_create():
    print("Entered Create. Id : " + id)
    return flash("Not yet implemented")

def api_read(id):
    print("Entered Read. Id : " + id)
    return flash("Not yet implemented")

def api_update(id):
    print("Entered Update. Id : " + id)
    return flash("Not yet implemented")

def api_delete(id):
    print("Entered Delete. Id : " + id)
    return flash("Not yet implemented")
"""
# send_email():

# Request
# Create
def request_form():
    print('request form is reached')
    return index()

def request_add():
    print('request add is reached')
    return index()

# Read
def request_all():
    print('detail request is reached')
    return index()

def request_detail(request_id):
    print(request_id)
    print('detail request is reached')
    return index()

# Update
def request_update(request_id):
    print(request_id)
    print('request update is reached')
    return index()

# Delete
def request_delete(request_id):
    print(request_id)
    print('request delete is reached')
    return index()

# API
# Create
def api_request_add():
    print('request add is reached')
    return index()

# Read
def api_request_all():
    print('detail request is reached')
    return index()

def api_request_detail(request_id):
    print(request_id)
    print('detail request is reached')
    return index()

# Update
def api_request_update(request_id):
    print(request_id)
    print('request update is reached')
    return index()

# Delete
def api_request_delete(request_id):
    print(request_id)
    print('request delete is reached')
    return index()
