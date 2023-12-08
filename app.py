"""Main entry point to the app."""
from __future__ import annotations

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from src.root import ROOT


def create_app() -> Flask:
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, template_folder="src/templates")
    csrf = CSRFProtect()
    csrf.init_app(app)
    csp = {
        "default-src": ["'self'", "cdn.jsdelivr.net"],
        "img-src": ["'self' data:"],
    }
    Talisman(app, force_https=False, content_security_policy=csp)
    app.config.from_prefixed_env()

    app.register_blueprint(ROOT)

    if app.debug is False:
        xray_recorder.configure(service="csd")
        XRayMiddleware(app, xray_recorder)

    return app


APP = create_app()
