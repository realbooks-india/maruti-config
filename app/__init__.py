from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
import os

# def create_app(config_class = Config):
app = Flask(__name__, instance_relative_config=True)
cors = CORS(app)

# Load the config file
if 'FLASK_APP_MODE' in os.environ.keys():
    app.config.from_object(os.environ['FLASK_APP_MODE'])
    print(os.environ['FLASK_APP_MODE'])
else:
    print('Develop Mode')
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)

from app.master import masterService

app.register_blueprint(masterService, url_prefix='/master')
# app.register_blueprint(reports)
# return app
