import json
import urllib.request

local = "http://127.0.0.1:5000"
remote = "http://reksti.herokuapp.com"
def test_api():
    path = ["/api/presence", "/api/presence/all"]

    data = {}
    data['owner'] = 'admin'

    headers = {'content-type': 'application/json'}

    json_data = json.dumps(data).encode('utf8')
    url = local+path[0]
    method = 'POST'

    req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
    response = urllib.request.urlopen(req)

    print(response.read())

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

def test_email():
    gmail_user = "waristea@gmail.com"
    gmail_password = "uubcprkertzvurnv"

    to = ["winaldojuan@gmail.com", "waristea@gmail.com"]
    subject = "Wibu"
    body = "Testing"
    send_email(gmail_user, to, subject, body, gmail_password)



if __name__=="__main__":
    test_api()
