
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, session
import authentification as auth
import calculate_score
import score_calculator
import timer
from score_calculator import read_ranking

app = Flask(__name__)
app.secret_key = 'acwo2024'

@app.route("/")
def first_function():

    username1=score_calculator.read_ranking()[0][0]
    score1=score_calculator.read_ranking()[0][1]
    username2=score_calculator.read_ranking()[1][0]
    score2=score_calculator.read_ranking()[1][1]
    username3=score_calculator.read_ranking()[2][0]
    score3=score_calculator.read_ranking()[2][1]
    username4=score_calculator.read_ranking()[3][0]
    score4=score_calculator.read_ranking()[3][1]
    username5=score_calculator.read_ranking()[4][0]
    score5=score_calculator.read_ranking()[4][1]
    username6=score_calculator.read_ranking()[5][0]
    score6=score_calculator.read_ranking()[5][1]
    username7=score_calculator.read_ranking()[6][0]
    score7=score_calculator.read_ranking()[6][1]
    username8=score_calculator.read_ranking()[7][0]
    score8=score_calculator.read_ranking()[7][1]
    username9=score_calculator.read_ranking()[8][0]
    score9=score_calculator.read_ranking()[8][1]
    username10=score_calculator.read_ranking()[9][0]
    score10=score_calculator.read_ranking()[9][1]
    username11=score_calculator.read_ranking()[10][0]
    score11=score_calculator.read_ranking()[10][1]
    username12=score_calculator.read_ranking()[11][0]
    score12=score_calculator.read_ranking()[11][1]

    return render_template("home.html", username1=username1,score1=score1,username2=username2,score2=score2,username3=username3,score3=score3,
                           username4=username4,score4=score4,username5=username5,score5=score5,username6=username6,score6=score6,
                           username7=username7,score7=score7,username8=username8,score8=score8,username9=username9,score9=score9,
                           username10=username10,score10=score10,username11=username11,score11=score11,username12=username12,score12=score12)



@app.route("/quizzes")
def second_function():
    return render_template("quiz_login.html")


# @app.route("/quiz_design",methods=['POST', 'GET'])
# def DESIGN():
#     if request.method == 'POST':
#         username = session.get('username')
#         ans_dict = {}
#         for i in range(1, 21, 1):
#             print(request.form.get(f'Q{i}'))
#             ans_dict[f'{i}'] = request.form.get(f'Q{i}')
#         print(ans_dict)
#     return render_template("DESIGN.html")
#
# @app.route("/quiz_beta",methods=['POST', 'GET'])
# def BETAFLIGHT():
#     return render_template("BETAFLIGHT.html")
#
# @app.route("/quiz_introducere",methods=['POST', 'GET'])
# def INTRODUCERE():
#     return render_template("INTRODUCERE.html")
#
# @app.route("/quiz_electronica",methods=['POST', 'GET'])
# def ELECTRONICA():
#     return render_template("ELECTRONICA.html")




@app.route("/submitted_beta",methods=['POST', 'GET'])
def submit_beta_function():
    if request.method == 'POST':
        username = session.get('username')
        ans_dict = {}
        for i in range(1, 16, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        score = calculate_score.read_qa(ans_dict,'quiz_BETAFLIGHT.json')
        submission_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        starting_time = auth.read_start_time(username,"starting_time_betaflight")
        time = timer.calculate_time_difference(starting_time,submission_time)
        auth.update_score(ans_dict,submission_time,score,username,"submission_time_betaflight",'score_BETAFLIGHT',
                          'ans_dict_betaflight',"total_time_betaflight", time)
        score_calculator.calculate_final_score()
        return redirect(url_for('loggedin_function'))

@app.route("/submitted_design",methods=['POST', 'GET'])
def submit_design_function():
    if request.method == 'POST':
        username = session.get('username')
        ans_dict = {}
        for i in range(1, 16, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        score = calculate_score.read_qa(ans_dict,'quiz_DESIGN.json')
        submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        starting_time = auth.read_start_time(username, "starting_time_design")
        time = timer.calculate_time_difference(starting_time, submission_time)
        auth.update_score(ans_dict, submission_time, score, username, "submission_time_design", 'score_DESIGN',
                          'ans_dict_design', "total_time_design", time)
        score_calculator.calculate_final_score()
        return redirect(url_for('loggedin_function'))

@app.route("/submitted_electronica",methods=['POST', 'GET'])
def submit_electronica_function():
    if request.method == 'POST':
        username = session.get('username')
        ans_dict = {}
        for i in range(1, 16, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        score = calculate_score.read_qa(ans_dict,'quiz_ELECTRONICA.json')
        submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        starting_time = auth.read_start_time(username, "starting_time_electronica")
        time = timer.calculate_time_difference(starting_time, submission_time)
        auth.update_score(ans_dict, submission_time, score, username, "submission_time_electronica", 'score_ELECTRONICA',
                          'ans_dict_electronica', "total_time_electronica", time)
        score_calculator.calculate_final_score()
        return redirect(url_for('loggedin_function'))

@app.route("/submitted_introducere",methods=['POST', 'GET'])
def submit_introducere_function():
    if request.method == 'POST':
        username = session.get('username')
        ans_dict = {}
        for i in range(1, 16, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        score = calculate_score.read_qa(ans_dict,'quiz_INTRODUCERE.json')
        submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        starting_time = auth.read_start_time(username, "starting_time_introducere")
        time = timer.calculate_time_difference(starting_time, submission_time)
        auth.update_score(ans_dict, submission_time, score, username, "submission_time_introducere", 'score_INTRODUCERE',
                          'ans_dict_introducere', "total_time_introducere", time)
        score_calculator.calculate_final_score()
        return redirect(url_for('loggedin_function'))



@app.route("/loggedin")
def loggedin_function():

    username = session.get('username')
    if username ==None:
        return render_template("home.html")
    username1=score_calculator.read_ranking()[0][0]
    score1=score_calculator.read_ranking()[0][1]
    username2=score_calculator.read_ranking()[1][0]
    score2=score_calculator.read_ranking()[1][1]
    username3=score_calculator.read_ranking()[2][0]
    score3=score_calculator.read_ranking()[2][1]
    username4=score_calculator.read_ranking()[3][0]
    score4=score_calculator.read_ranking()[3][1]
    username5=score_calculator.read_ranking()[4][0]
    score5=score_calculator.read_ranking()[4][1]
    username6=score_calculator.read_ranking()[5][0]
    score6=score_calculator.read_ranking()[5][1]
    username7=score_calculator.read_ranking()[6][0]
    score7=score_calculator.read_ranking()[6][1]
    username8=score_calculator.read_ranking()[7][0]
    score8=score_calculator.read_ranking()[7][1]
    username9=score_calculator.read_ranking()[8][0]
    score9=score_calculator.read_ranking()[8][1]
    username10=score_calculator.read_ranking()[9][0]
    score10=score_calculator.read_ranking()[9][1]
    username11=score_calculator.read_ranking()[10][0]
    score11=score_calculator.read_ranking()[10][1]
    username12=score_calculator.read_ranking()[11][0]
    score12=score_calculator.read_ranking()[11][1]
    time_introducere = score_calculator.read_quiz_score(username,'total_time_introducere')
    time_electronica = score_calculator.read_quiz_score(username, 'total_time_electronica')
    time_design = score_calculator.read_quiz_score(username, 'total_time_design')
    time_beta = score_calculator.read_quiz_score(username, 'total_time_betaflight')
    score_introducere = score_calculator.read_quiz_score(username,'score_INTRODUCERE')
    score_electronica = score_calculator.read_quiz_score(username, 'score_ELECTRONICA')
    score_design = score_calculator.read_quiz_score(username, 'score_DESIGN')
    score_betaflight = score_calculator.read_quiz_score(username, 'score_BETAFLIGHT')



    return render_template("loggedin.html", username1=username1,score1=score1,username2=username2,score2=score2,username3=username3,score3=score3,
                           username4=username4,score4=score4,username5=username5,score5=score5,username6=username6,score6=score6,
                           username7=username7,score7=score7,username8=username8,score8=score8,username9=username9,score9=score9,
                           username10=username10,score10=score10,username11=username11,score11=score11,username12=username12,score12=score12,
                           total_time_introducere=time_introducere,total_time_electronica=time_electronica,total_time_design=time_design,total_time_betaflight=time_beta,
                           score_introducere=score_introducere,score_electronica=score_electronica,score_design=score_design,score_betaflight=score_betaflight,username=username)

@app.route("/login", methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        name = request.form["name"]
        password = str(request.form["Password"])
        if auth.check_password(name, password):
            session['username']=name
            print(session['username'])
            return redirect(url_for('loggedin_function'))
    return render_template("login.html")

@app.route("/quiz_login", methods=['POST', 'GET'])
def quiz_login():
    if request.method == 'POST':
        quiz_name = request.form.get("quiz_login")
        code = str(request.form["name-2"])
        print(quiz_name,code)
        username = session.get('username')
        print(username)
        if quiz_name == 'INTRODUCERE':
            if auth.check_time(username,'starting_time_introducere'):
                if auth.check_quiz_password(quiz_name, code):
                    starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    quiz_starting_time_name = 'starting_time_introducere'
                    auth.update_starting_time(starting_time, username, quiz_starting_time_name)
                    return render_template('INTRODUCERE.html')
                else:
                    return render_template("quiz_login.html")
            else:
                return render_template("quiz_login.html")

        elif quiz_name=='ELECTRONICA':
            if auth.check_time(username, 'starting_time_electronica'):
                if auth.check_quiz_password(quiz_name, code):
                    starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    quiz_starting_time_name = 'starting_time_electronica'
                    auth.update_starting_time(starting_time, username, quiz_starting_time_name)
                    return render_template('ELECTRONICA.html')
                else:
                    return render_template("quiz_login.html")
            else:
                return render_template("quiz_login.html")

        elif quiz_name=='DESIGN':
            if auth.check_time(username, 'starting_time_design'):
                if auth.check_quiz_password(quiz_name, code):
                    starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    quiz_starting_time_name = 'starting_time_design'
                    auth.update_starting_time(starting_time, username, quiz_starting_time_name)
                    return render_template('DESIGN.html')
                else:
                    return render_template("quiz_login.html")
            else:
                return render_template("quiz_login.html")
        else:
            if auth.check_time(username, 'starting_time_betaflight'):
                if auth.check_quiz_password(quiz_name, code):
                    starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    quiz_starting_time_name = 'starting_time_betaflight'
                    auth.update_starting_time(starting_time, username, quiz_starting_time_name)
                    return render_template('BETAFLIGHT.html')
                else:
                    return render_template("quiz_login.html")
            else:
                return render_template("quiz_login.html")
    else:
        return render_template("quiz_login.html")



@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('first_function'))


if __name__ == '__main__':
    app.run(debug=True)
