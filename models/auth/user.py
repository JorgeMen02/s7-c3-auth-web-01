from flask_login import UserMixin
from utils.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False, unique=True)
    mensaje = db.Column(db.String(80), nullable=False)

    def __init__(self, nombre, mensaje) -> None:
        self.nombre = nombre
        self.mensaje = mensaje

    def __repr__(self) -> str:
        return f"User({self.id}, '{self.nombre}', '{self.mensaje}')"
