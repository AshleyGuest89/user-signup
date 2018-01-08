from flask import Flask, request, redirect, render_template
import cgi
import os




app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if username == "":
        username_error = "This is a required field"

    if username != "":    
        if " " in username:
            username_error = "No spaces allowed in username"
        if len(username) < 3 or len(username) > 20:
            username_error = "Username must be 3 - 20 characters"
        
    if password == "":
        password_error = "This is a required field"
        
    if password != "":    
        if len(password) < 3 or len(password) > 20:
            password_error = "Password must be 3 - 20 characters"
        
    if verify == "":
        verify_error = "This is a required field"

    if password != verify:
        verify_error="Passwords do not match!"

    if email != "":
        if "@" not in email or "." not in email or " " in email:
            email_error = "Not a valid email address"
        
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters"

    if not username_error and not password_error and not verify_error and not email_error:
        name = username
        return redirect('/welcome?name={0}'.format(name))
    else:
        password = ""
        verify = ""
        return render_template('index.html', username = username, username_error = username_error,
        password = password, password_error = password_error, verify = verify, 
        verify_error = verify_error, email = email, email_error = email_error)
        


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    username = request.args.get('name')
    return render_template('welcome.html', name = username)

app.run()