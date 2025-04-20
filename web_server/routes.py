from web_server import app
from wtforms import PasswordField
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    passfield = PasswordField("secret-key")
    return render_template("register.html", passwd = passfield)