"""Root blueprint."""
from flask import Blueprint, render_template

ROOT = Blueprint("root", __name__)


@ROOT.route("/")
def hello_world() -> str:
    """Return main page."""
    return render_template("hello.html")
