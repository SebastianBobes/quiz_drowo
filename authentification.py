import json


def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())
        return creds

def check_password(username, password):
    creds = read_credentials()
    for i in creds:
        if i['user']==username:
            if i['password']==password:
                return True
    return False

def check_quiz_password(quiz_name,code):
    creds = read_credentials(path='quiz_auth.json')
    for i in creds:
        if i['user'] == quiz_name:
            if i['password'] == code:
                return True
    return False
