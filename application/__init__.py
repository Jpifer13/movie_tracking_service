from flask import Flask
# from flask_marshmallow import Marshmallow
from config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object(config)
CORS(flask_app)
db = SQLAlchemy(flask_app)
# marshmallow_app = Marshmallow(flask_app)

from application import routes, models
