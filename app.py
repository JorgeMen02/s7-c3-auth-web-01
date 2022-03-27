from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth

app = Flask(__name__)

# configurar flask alchemy
app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(auth)
