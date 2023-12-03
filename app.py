"""Main entry point to the app."""
import logging

import sentry_sdk
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

APP = Flask(__name__, template_folder="src/templates")
CSRF = CSRFProtect()
CSRF.init_app(APP)


sentry_sdk.init(
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    enable_tracing=True,
    auto_session_tracking=True,
    debug=True,
)

ASGI = WsgiToAsgi(APP)


@APP.route("/")
def hello_world() -> str:
    """Return main page."""
    logging.error("Hello, World!")

    return render_template("hello.html")
