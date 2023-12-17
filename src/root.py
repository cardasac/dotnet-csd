"""Root blueprint."""
from __future__ import annotations

import base64
from io import BytesIO

import numpy as np
from flask import (
    Blueprint,
    Response,
    redirect,
    render_template,
    request,
    url_for,
)
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle

from src.blood_pressure import calculate_blood_pressure
from src.forms import BloodPressureForm

ROOT = Blueprint("root", __name__)


@ROOT.post("/")
def submit() -> str | Response:
    """Submit the form."""
    form = BloodPressureForm()

    if form.validate_on_submit():
        systolic = request.form.get("systolic", type=int)
        diastolic = request.form.get("diastolic", type=int)
        result = calculate_blood_pressure(systolic, diastolic)

        return redirect(
            url_for(
                "root.success",
                result=result,
                systolic=systolic,
                diastolic=diastolic,
            ),
        )

    return render_template("content.html", form=form)


@ROOT.get("/")
def get_form() -> str:
    """Get the form."""
    return render_template("content.html", form=BloodPressureForm())


@ROOT.get("/result")
def success() -> str:
    """Show the result."""
    result = request.args.get("result", default=None, type=str)
    systolic = request.args.get("systolic", default=None, type=int)
    diastolic = request.args.get("diastolic", default=None, type=int)
    x_y_coordinates = (40, 70)

    fig = Figure()
    ax = fig.subplots()

    ax.scatter(diastolic, systolic, marker="x", s=100, zorder=6, color="black")

    ax.set_yticks(np.arange(70, 200, 10))
    ax.set_xticks(np.arange(40, 110, 10))

    ax.add_patch(Rectangle(x_y_coordinates, 20, 20, color="indigo", zorder=5))
    ax.add_patch(Rectangle(x_y_coordinates, 40, 50, color="green", zorder=4))
    ax.add_patch(Rectangle(x_y_coordinates, 50, 70, color="yellow", zorder=3))
    ax.add_patch(Rectangle(x_y_coordinates, 60, 120, color="red", zorder=2))

    ax.set_ylabel("Systolic")
    ax.set_xlabel("Diastolic")
    ax.set_title("Blood Pressure Levels")

    with BytesIO() as buf:
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("success.html", result=result, img_data=data)
