#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from logging.handlers import TimedRotatingFileHandler

from flask_migrate import Migrate

from application.core.utils.log_formatter import NewsLogsFormatter
from flask import Flask, g, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_file_location=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/haber_takip_api"
    db.init_app(app)
    with app.app_context():
        migrate = Migrate(app, db)
        CORS(app)
        if config_file_location:
            app.config.from_pyfile(filename=config_file_location, silent=False)
        else:
            app.config.from_pyfile('../config/dev.cfg', silent=False)
        from application.core.models import NEWS
        db.app = app
        db.create_all()
        db.session.commit()

    # configure logging
    log_format = (
        "[%(asctime)s] %(levelname)s %(remote_addr)s %(request_type)s %(http_version)s %(url)s %(pathname)s rt:%(response_time)s %(message)s")
    log_formatter = NewsLogsFormatter(log_format)
    log_file = app.config['LOG_FILE_PATH']
    log_timed_rotating_handler = TimedRotatingFileHandler(log_file, when="midnight")
    log_timed_rotating_handler.setFormatter(log_formatter)
    log_timed_rotating_handler.setLevel(app.config['LOG_LEVEL'])
    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(log_timed_rotating_handler)

    # configure before first request
    @app.before_first_request
    def before_first_request():
        g.start = time.time()

    @app.before_request
    def before_request():
        g.start = time.time()

    load_blueprints(app)
    return app


def load_blueprints(app):
    from application.api.controller import mod_api
    app.register_blueprint(mod_api)