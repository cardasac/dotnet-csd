"""Main entry point to the app."""
from __future__ import annotations

import sentry_sdk
from flask import Flask
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware
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

    if app.config["TESTING"] is False:
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
            integrations=[FlaskIntegration()],
        )

    return app


APP = SentryWsgiMiddleware(create_app())
