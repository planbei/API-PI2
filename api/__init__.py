from flask import Flask
from .extensions import db, api
from .resources import add_namespaces
from config import Config
from markupsafe import escape


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config())

    db.init_app(app)
    api.init_app(app)

    add_namespaces(api)

    return app
