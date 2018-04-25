#project/controllers.py
from flask import flash, render_template, request, session, redirect, url_for, json, jsonify
from flask_login import current_user, login_user, logout_user
import smtplib

# Reminder:
# - Buat jadwal
# - Query user based on name
# - Implement absen ke api
# - Buat form input (banyak..)

def index():
    if current_user.is_authenticated:
        print(current_user.get_id())
        return render_template('dashboard.html')
    else:
        return render_template('login.html')

def login():
    # if login is being done
    if request.method=='POST':
        # check login credentials
        from project.models import User
        from werkzeug import check_password_hash

        if request.form['email'] != None and request.form['password'] != None:
            user = User.query.filter_by(email=request.form['email']).first()
            password = request.form['password']

            if user and check_password_hash(user.password, password):
                if user.admin:
                    print("Logged in!")
                    login_user(user)
                else:
                    print("Credentials true, but not an admin")
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
    logout_user()
    session.pop('logged_in', None)
    return redirect(url_for('index'))

# Untuk RekSTI
# API
# Create
def api_presence_add():
    from project import app
    print("Mark 0")
    json_data = request.get_json()
    print(json_data)
    user_name = json["owner"]
    user = User.query.filter_by(name=user_name).first()

    data = {}
    print("Mark 1")
    if user==None:
        print("Mark 2a")
        data['status'] = 'failed'
        data['message'] = 'person is not registered'
    else:
        print("Mark 1b")
        presence = Presence.query.filter_by(owner=user.id).first()
        if (presence==None):
            presence = Presence(user.id)
            try:
                print("Mark 2a")

                db.session.add(presence)
                db.session.commit()

                gmail_user = "waristea@gmail.com"
                gmail_password = "uubcprkertzvurnv"

                to = [user.email]
                subject = "Notification"
                body = "You are marked as present. Here are your schedules: sdfsaff"

                send_email(gmail_user, to, subject, body, gmail_password)

                data['status'] = 'successful'
                data['message'] = 'user is marked as present'
                data['user'] = jsonify(user)

            except Exception as e:
                print("Mark 2b")
                data['status'] = 'failed'
                data['message'] = 'expection occured, please contact admin'
                print(e)
            db.session.close()
        else:
            print("Mark 2c")

            data['status'] = 'successful'
            data['message'] = 'user has already been marked as present'
            data['user'] = jsonify(user)

    print("Yes")

    response = app.response_class(
        response = json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
# Read
def api_presence_all():
    from project import app

    #json_data = request.get_json()
    #print(json_data)# Seharusnya gk ada

    data = {'status' : 'successful'}

    response = app.response_class(
        response = json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

def api_presence_detail_by_user(user_id):
    from project import app

    #json_data = request.get_json()
    #print(json_data)

    data = {'status' : 'successful'}

    response = app.response_class(
        response = json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

def api_presence_detail_by_id(presence_id):
    from project import app

    #json_data = request.get_json()
    #print(json_data)

    data = {'status' : 'successful'}

    response = app.response_class(
        response = json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
# Update
def api_presence_update(presence_id):
    from project import app

    json_data = request.get_json()
    print(json_data)

    data = {'status' : 'successful'}

    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype='application/json'
    )
    return response

# Delete
def api_presence_delete(presence_id):
    from project import app

    json_data = request.get_json()
    print(json_data)

    data = {'status' : 'successful'}

    response = app.response_class(
        response = json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# Gunakan password dan username yagn disediakan google
def send_email(from_addr, to_addr_list, subject, body, gmail_password, smtp_server = 'smtp.gmail.com', port = 465):
    import smtplib

    header = 'From : ' + from_addr
    header += 'To : '
    header.join(to_addr_list)
    header += 'Subject : ' + subject

    message = header + body
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP("smtp.gmail.com", 587)
    server_ssl.ehlo() # optional, called by login()
    server_ssl.starttls()
    server_ssl.login(from_addr, gmail_password)
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
    server_ssl.sendmail(from_addr, to_addr_list, message)
    #server_ssl.quit()
    server_ssl.quit()
    print('successfully sent the mail')

# Untuk IMKA
# IoT related methods
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
