from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/register")
def register():
    return render_template("register.html")


@auth.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
