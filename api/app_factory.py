import logging
from flask import Flask
from configs import config


def create_flask_app():
    app = Flask(__name__)
    app.config.from_mapping(config.model_dump())
    return app


def create_app_init():
    app = create_flask_app()
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    from extensions import (
        ext_app_metrics,
        ext_blueprints,
        ext_login,
    )

    extensions = [
        ext_app_metrics,
        ext_blueprints,
        ext_login,
    ]
    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            if config.DEBUG:
                logging.info(f"Skipped {short_name}")
            continue
        ext.init_app(app)


def create_migrations_app():
    app = create_flask_app()
    from extensions import ext_database, ext_migrate
    ext_database.init_app(app)
    ext_migrate.init_app(app)
    return app
