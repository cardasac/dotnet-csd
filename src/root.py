"""Root blueprint."""
import logging

from flask import Blueprint, render_template

ROOT = Blueprint("root", __name__)


@ROOT.route("/")
def hello_world() -> str:
    """Return main page."""
    logging.error("Hello, World!")

    return render_template("hello.html")
