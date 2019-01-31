from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/signin", methods=["POST"])
def user_signin():
    username_error = ""
    password_error = ""
    email_error = ""

    if not username:
        username_error = "Please input a username"

    elif len(username) > 3 or len(username) < 20:
        username_error = "Please input a valid username between 3 and 20 characters."

    else:
        username = username

    if not password:
        password_error = "Please input a password"
    
    elif password != password_v:
        password_error = "Please ensure passwords match"
    
    elif len(password) < 3 or len(password) > 20:
        password_error = "Please input a password between 3 and 20 characters"

    else:
        continue

    if not username_error and not password_error and not email_error:
        username = username
        return render_template("signin.html", username=username)
    else:
        render_template("edit.html", 
        username_error = username_error,
        password_error = password_error,
        email_error = email_error,
        username = username,
        email = email)

@app.route("/")
def index():
    username = ""
    email = ""
    encoded_error = request.args.get("error")
    return render_template('edit.html', username=username, email=email)

app.run()