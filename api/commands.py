import logging
import click


@click.command("upgrade-db", help="Upgrade the database")
def upgrade_db():
    try:
        click.echo(click.style("Starting database migration.", fg="green"))

        # run db migration
        import flask_migrate

        flask_migrate.upgrade()

        click.echo(click.style("Database migration successful!", fg="green"))

    except Exception:
        logging.exception("Failed to execute database migration")
