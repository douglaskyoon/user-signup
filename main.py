from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/welcome", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error=''
    password_error=''
    verify_error=''
    email_error=''

    if len(username) < 3 or len(username) > 20:
        username_error="that is not a valid username"
        

    if len(password) < 3 or len(password) > 20:
        password_error="that is not a valid password"
        

    if password != verify:
        verify_error = "password does not match"

    count_1 = 0
    count_2 = 0
    count_3=0
    for x in email:
        if ord(x) == 64:
            count_1 += 1
        if ord(x) == 46:
            count_2 += 1
        if ord(x) == 32:
            count_3 += 1
    if count_3 != 0 or count_1 != 1 or count_2 != 1 or len(email) < 3 or len(email) >20:
        email_error = "that is not a valid email"

    if not username_error and not password_error and not verify_error and not email:

        return render_template('welcome.html', username=username)

    elif not username_error and not password_error and not verify_error and not email_error:

        return render_template('welcome.html', username=username)

    else:
        return render_template('signup.html', 
            username_error=username_error, 
            password_error=password_error, 
            verify_error=verify_error,
            email_error=email_error,
            email_input=email,
            username_input=username)



@app.route("/")
def index():
    return render_template('signup.html')

app.run()