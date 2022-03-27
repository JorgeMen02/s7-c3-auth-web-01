from flask import Blueprint, render_template, redirect, url_for
from models.auth.user import User
from forms.registerForm import Messages
from utils.db import db

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("HomePage.htm")


@auth.route("/messages", methods=["GET", "POST"])
def messages():
    form = Messages()
    if form.validate_on_submit():
        # data that comes from the form
        nombre = form.nombre.data
        mensaje = form.mensaje.data
        # encrypt password
        newUser = User(nombre, mensaje)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("auth.home"))
    return render_template("HomePage.htm", form=form)
