"""Root blueprint."""
from flask import Blueprint, render_template, request
from src.blood_pressure import calculate_blood_pressure
from src.forms import MyForm

ROOT = Blueprint("root", __name__)


@ROOT.route("/", methods=["GET", "POST"])
def submit():
    form = MyForm()

    if form.validate_on_submit():
        systolic = request.form.get("systolic", type=int)
        diastolic = request.form.get("diastolic", type=int)
        result = calculate_blood_pressure(systolic, diastolic)

        return render_template("content.html", form=form, result=result)

    return render_template("content.html", form=form)
