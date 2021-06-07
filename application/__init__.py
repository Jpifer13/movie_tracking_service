from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)
    CORS(flask_app)
    register_routes(flask_app)
    db.init_app(flask_app)

    return flask_app

def register_routes(application) -> None:
    with application.app_context():
        import application.controllers as controllers
        blueprints = [
            controllers.routes.urls
        ]

        for blueprint in blueprints:
            application.register_blueprint(blueprint, url_prefix='')
