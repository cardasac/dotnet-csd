from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi

application = Flask(__name__, template_folder="src/templates")
@application.route("/")
def hello_world():
    return render_template("hello.html")

asgi_app = WsgiToAsgi(application)
