import flask_migrate  # type: ignore
from models import db


def init_app(app):
    flask_migrate.Migrate(app, db)
