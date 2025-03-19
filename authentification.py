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
        if i['name'] == quiz_name:
            if i['code'] == code:
                return True
    return False

def update_score(ans_dict,submission_time,score,username,quiz_submission_time_name,quiz_score_name,ans_dict_name,total_time_name,total_time,path = "auth.json"):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            dict[quiz_score_name] = score
            dict[quiz_submission_time_name] = submission_time
            dict[ans_dict_name] = ans_dict
            dict[total_time_name] = total_time
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))

def update_starting_time(starting_time,username,starting_time_name,path = 'auth.json'):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            dict[starting_time_name] = starting_time
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))

def check_time(username,quiz_name_time):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            if dict[quiz_name_time] =="":
                return True
            else:
                return False

def read_start_time(username,time_name):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            return dict[time_name]


