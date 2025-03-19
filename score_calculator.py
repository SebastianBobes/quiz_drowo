
import json
def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())
        return creds


def calculate_final_score(path: str = "auth.json"):
    credentials = read_credentials()
    for dict in credentials:
        if dict['total_time_introducere']!="":
            quiz_score_introducere = dict['score_INTRODUCERE'] * 10
            time_introducere = int(float(dict['total_time_introducere'].replace(":", ".")))
            time_score_introducere = (14 - time_introducere) * 3
            final_score_introducere =  quiz_score_introducere + time_score_introducere

        else:
            final_score_introducere=0

        if dict['total_time_electronica'] != "":
            quiz_score_electronica = dict['score_ELECTRONICA'] * 10
            time_electronica = int(float(dict['total_time_electronica'].replace(":", ".")))
            time_score_electronica = (14 - time_electronica) * 3
            final_score_electronica = quiz_score_electronica + time_score_electronica
        else:
            final_score_electronica = 0

        if dict['total_time_design'] != "":
            quiz_score_design = dict['score_DESIGN'] * 10
            time_design = int(float(dict['total_time_design'].replace(":", ".")))
            time_score_design = (14 - time_design) * 3
            final_score_design = quiz_score_design + time_score_design

        else:
            final_score_design = 0

        if dict['total_time_betaflight'] != "":
            quiz_score_betaflight = dict['score_BETAFLIGHT'] * 10
            time_betaflight = int(float(dict['total_time_betaflight'].replace(":", ".")))
            time_score_betaflight = (14 - time_betaflight) * 3
            final_score_betaflight = quiz_score_betaflight + time_score_betaflight

        else:
            final_score_betaflight = 0

        dict['final_score'] = final_score_betaflight+final_score_electronica+final_score_introducere+final_score_design
    with open(path, 'w+') as f:
        f.write(json.dumps(credentials, indent=4))

def read_ranking():
    ranking_dict = {}
    credentials = read_credentials()
    for dict in credentials:
        name = dict['user']
        ranking_dict[name] = dict['final_score']
    sorted_dict = sorted(ranking_dict.items(), key=lambda item: item[1], reverse=True)
    string = ""
    for item in sorted_dict:
        string = string + f"{item[0]}: {item[1]}\n"
    return sorted_dict


if __name__ == '__main__':
    ranking  = read_ranking()
    print(ranking)




