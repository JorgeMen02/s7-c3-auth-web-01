from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class Messages(FlaskForm):
    nombre_completo = StringField(
        validators=[InputRequired(), Length(min=4, max=20)],
        render_kw={"placeholder": "Nombre completo"},
    )
    mensaje = StringField(
        validators=[InputRequired(), Length(min=4, max=100)],
        render_kw={"placeholder": "Mensaje"},
    )
    submit = SubmitField("register")
