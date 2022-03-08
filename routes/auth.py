from flask import Blueprint, render_template, redirect, url_for
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from utils.bcryptService import bcrypt
from models.auth.user import User
from utils.db import db

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # data that comes from the form
        username = form.username.data
        password = form.password.data
        # encrypt password
        hashed_password = bcrypt.generate_password_hash(password)
        newUser = User(username, hashed_password)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
