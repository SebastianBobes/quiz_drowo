from flask import Flask, render_template, request, redirect, url_for, session
import authentification as auth


app = Flask(__name__)
app.secret_key = 'acwo2024'

@app.route("/")
def first_function():
    return render_template("home.html")

@app.route("/quizzes")
def second_function():
    return render_template("quiz_login.html")

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
        code = str(request.form["Password"])
        print(quiz_name,code)
    return render_template("quiz_login.html")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('first_function'))


if __name__ == '__main__':
    app.run(debug=True)
