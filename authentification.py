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
