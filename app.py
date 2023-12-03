"""Main entry point to the app."""
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

APP = Flask(__name__, template_folder="src/templates")
CSRF = CSRFProtect()
CSRF.init_app(APP)

ASGI = WsgiToAsgi(APP)

@APP.route("/")
def hello_world() -> str:
    """Return main page."""
    return render_template("hello.html")
