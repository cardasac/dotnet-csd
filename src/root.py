import logging

from flask import Blueprint, render_template

root = Blueprint("root", __name__)


@root.route("/")
def hello_world() -> str:
    """Return main page."""
    logging.error("Hello, World!")

    return render_template("hello.html")
