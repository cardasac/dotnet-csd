"""Main forms for the server."""
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange


class BloodPressureForm(FlaskForm):
    """Form for blood pressure."""

    systolic = IntegerField(
        "Systolic",
        validators=[InputRequired(), NumberRange(min=70, max=190)],
    )
    diastolic = IntegerField(
        "Diastolic",
        validators=[InputRequired(), NumberRange(min=40, max=100)],
    )
