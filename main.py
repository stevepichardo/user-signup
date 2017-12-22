from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template("form.html")

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    if password != verifypassword:
        return "Try Again"
    return redirect("/welcome?username={0}".format(username))

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html",username=username)



app.run()