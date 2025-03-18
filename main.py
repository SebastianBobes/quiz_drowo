from flask import Flask, render_template, request, redirect, url_for, session
import authentification as auth
import calculate_score


app = Flask(__name__)
app.secret_key = 'acwo2024'

@app.route("/")
def first_function():
    return render_template("home.html")

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
        print(username)
        print(ans_dict)
        score = calculate_score.read_qa(ans_dict,'quiz_BETAFLIGHT.json')
        print(score)
        return redirect(url_for('loggedin_function'))




@app.route("/submitted_design")
def submit_design_function():
    pass

@app.route("/submitted_electronica")
def submit_electronica_function():
    pass

@app.route("/submitted_introducere")
def submit_introducere_function():
    pass



@app.route("/loggedin")
def loggedin_function():
    username = session.get('username')
    if username ==None:
        return render_template("home.html")
    return render_template('loggedin.html', username=username)

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
        if auth.check_quiz_password(quiz_name, code):
            return render_template(f"{quiz_name}.html")
    return render_template("quiz_login.html")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('first_function'))


if __name__ == '__main__':
    app.run(debug=True)
