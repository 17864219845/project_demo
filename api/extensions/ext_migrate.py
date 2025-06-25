def init_app(app):
    import flask_migrate  # type: ignore
    from models import db
    flask_migrate.Migrate(app, db)
