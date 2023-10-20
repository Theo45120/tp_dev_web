from .app import app
from flask import render_template
from .models import get_sample
from flask_login import login_user, current_user
from flask import request, redirect, url_for


@app.route("/")
def home():
    return render_template(
        "booksBS.html", 
        title="My Books !",
        books=get_sample())


@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template(
        "detail.html",
        book=book)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from .models import User
from hashlib import sha256

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest ()
        return user if passwd == user.password else None

@app.route("/login/", methods=("GET","POST",))
def login():
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=f)

from flask_login import logout_user
@app.route("/logout/")
def logout():
    logout_user ()
    return redirect(url_for("home"))