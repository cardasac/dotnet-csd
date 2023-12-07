"""Main forms for the server."""
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange


class MyForm(FlaskForm):
    """Form for blood pressure."""

    systolic = IntegerField(
        "systolic",
        validators=[DataRequired(), NumberRange(min=70, max=190)],
    )
    diastolic = IntegerField(
        "diastolic",
        validators=[DataRequired(), NumberRange(min=40, max=80)],
    )
