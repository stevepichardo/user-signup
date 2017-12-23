from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    error_dict = {}
    username = ''
    email = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verifypassword = request.form['verifypassword']
        email = request.form['email']

        if (len(username) < 3 or len(username) > 20) or " " in username:
            error_dict['username'] = "Not a valid username"
        
        if len(password) < 3 or len(password) > 20 or " " in password:
            error_dict['password'] = "not a valid password"

        if password != verifypassword:
            error_dict['verifypassword'] = "Passwords do not match"
        
        if email:
            if "@" not in email or "." not in email:
                error_dict['email'] = "invalid email"
        
        if not error_dict:
            return redirect("/welcome?username={0}".format(username))
    
    return render_template("form.html", error_dict=error_dict, username=username, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html",username=username)



app.run()