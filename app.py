"""Main entry point to the app."""
from __future__ import annotations

import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask, render_template
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from werkzeug.exceptions import HTTPException

from werkzeug.middleware.proxy_fix import ProxyFix
from src import db
from src.auth import AUTH
from src.root import ROOT


def handle_exception(error: HTTPException) -> str:
    """Handle all exceptions."""
    return render_template("500_generic.html", error=error.description)


def create_app(app_config: dict | None = None) -> Flask:
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, template_folder="src/templates")
    csrf = CSRFProtect()
    csrf.init_app(app)
    csp = {
        "default-src": ["'self'"],
        "img-src": ["'self' data:"],
        "frame-ancestors": ["'none'"],
        "form-action": ["'self'"],
    }

    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    Talisman(
        app,
        force_https=False,
        frame_options="DENY",
        content_security_policy=csp,
    )
    compress = Compress()
    compress.init_app(app)
    app.config.from_prefixed_env()

    db.init_app(app)

    app.register_error_handler(HTTPException, handle_exception)
    app.register_blueprint(ROOT)
    app.register_blueprint(AUTH)

    if os.getenv("AWS_XRAY_TRACING_NAME", None):
        xray_recorder.configure(
            service="csd",
            dynamic_naming="*.alviralex.com",
            plugins=("ElasticBeanstalkPlugin", "EC2Plugin"),
        )
        XRayMiddleware(app, xray_recorder)

    app.config.from_mapping(app_config)

    return app
