import json
import urllib.request
from project.controllers import send_email

local = "http://127.0.0.1:5000"
remote = "http://reksti.herokuapp.com"
def test_api():
    path = ["/api/presence", "/api/presence/all"]

    data = {'testing': 'It is a success'}
    headers = {'content-type': 'application/json'}

    json = json.dumps(data).encode('utf8')
    url = local+path[0]
    method = 'POST'

    req = urllib.request.Request(url, data=json, headers=headers, method=method)
    response = urllib.request.urlopen(req)

    print(response.read())

def test_email():
    gmail_user = "waristea@gmail.com"
    gmail_password = "uubcprkertzvurnv"

    to = ["winaldojuan@gmail.com", "waristea@gmail.com"]
    subject = "Wibu"
    body = "Testing"

    send_email(gmail_user, to, subject, body, gmail_password)

if __name__=="__main__":
    test_email()
