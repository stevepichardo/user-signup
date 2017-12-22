from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template("form.html")

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    return redirect("/welcome")

@app.route("/welcome")
def welcome():
    return "hello"



app.run()