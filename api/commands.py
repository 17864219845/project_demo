import logging
import os

import click


@click.command("upgrade-db", help="Upgrade the database")
def upgrade_db():
    try:
        click.echo(click.style("Starting database migration.", fg="green"))
        import flask_migrate
        if not os.path.exists("migrations"):
            click.echo(click.style("Migrations folder not found. Running init.", fg="yellow"))
            flask_migrate.init()
            flask_migrate.migrate()  # 自动生成迁移脚本
        flask_migrate.upgrade()  # 应用迁移到数据库

        click.echo(click.style("Database migration successful!", fg="green"))

    except Exception:
        logging.exception("Failed to execute database migration")
