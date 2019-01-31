from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/")
def signin():
    return render_template('edit.html')

@app.route("/", methods=["POST"])
def user_signin():
    username = cgi.escape(request.form["username"])
    email = cgi.escape(request.form["email"])
    password =  cgi.escape(request.form["password"])
    password_v =  cgi.escape(request.form["password_v"])
    username_error = ""
    password_error = ""
    email_error = ""

    if not username:
        username_error = "Please input a username"

    elif len(username) < 3 or len(username) > 20:
        username_error = "Please input a valid username between 3 and 20 characters."

    else:
        username = request.form["username"]

    if not password:
        password_error = "Please input a password"
    
    elif password != password_v:
        password_error = "Please ensure passwords match"
    
    elif len(password) < 3 or len(password) > 20:
        password_error = "Please input a password between 3 and 20 characters"

    if not email and  not username_error and not password_error and not email_error:
        username = request.form["username"]
        return redirect("/signin?username={0}".format(username))
    
    elif "@" in email and "." in email and not " " in email:
        username = request.form["username"]
        return redirect("/signin?username={0}".format(username))

    else:
        email_error = "Please enter a valid email."

    return render_template("edit.html", 
        username_error = username_error,
        password_error = password_error,
        email_error = email_error,
        username = username,
        email = email)

@app.route('/signin')
def valid_signin():
    username = request.args.get("username")
    return render_template("signin.html", username = username)

app.run()