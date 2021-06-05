from flask import Flask
from config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object(config)
CORS(flask_app)
db = SQLAlchemy(flask_app)

from application import routes, models
