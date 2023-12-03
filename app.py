"""Main entry point to the app."""
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

application = Flask(__name__, template_folder="src/templates")
csrf = CSRFProtect()
csrf.init_app(application)
@application.route("/")
def hello_world():
    return render_template("hello.html")

asgi_app = WsgiToAsgi(application)
