import json

def read_qa(ans_dict,path):
    score=0
    with open(path, 'r') as f:
        x = json.loads(f.read())
        for index in x:
            if x[index] == ans_dict[index]:
                score+=1
        return(score)

