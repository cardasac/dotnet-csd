"""Main entry point to the app."""

import sentry_sdk
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware
from src.root import ROOT


def create_app(test_config: None | dict = None) -> Flask:
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, template_folder="src/templates")
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.register_blueprint(ROOT)

    if test_config is None:
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
        )

    return app


APP = SentryWsgiMiddleware(create_app())
