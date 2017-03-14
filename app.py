import logging
from flask import Flask
from sqlalchemy import orm

from fo import config

from fo.extensions import db, login_manager, migrate
from admin import create_admin


def create_app():
    app = Flask(__name__)

    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(messages)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    app.logger_name = config.LOGGER_NAME
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.config.from_object(config)

    # register extensions
    from fo.models import User
    from fo.models import Registration
    orm.configure_mappers()
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    admin = create_admin(app)
    from fo.views import blueprint

    app.register_blueprint(blueprint)
    return app
