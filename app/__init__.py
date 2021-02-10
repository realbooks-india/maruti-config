from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from botocore.config import Config
from flask_jwt_extended import JWTManager
import redis
import boto3
import os

# def create_app(config_class = Config):
app = Flask(__name__, instance_relative_config=True)
cors = CORS(app)
jwt = JWTManager(app)

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
rd = redis.StrictRedis(host=app.config['REDIS_URI'], port=6379, charset="utf-8", decode_responses=True)

# DynamoDB Database
my_config = Config(
    region_name = app.config['AWS_REGION'],
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

dynamodb = boto3.resource('dynamodb', endpoint_url=app.config['DYNAMODB_URI'], 
                                        config=my_config,
                                        aws_access_key_id=app.config['AWS_ACCESS_KEY'],
                                        aws_secret_access_key=app.config['AWS_SECRET_KEY'])

from app.master import masterService
from app.report import reportService
from app.users import usersService 

app.register_blueprint(masterService, url_prefix='/master')
app.register_blueprint(reportService, url_prefix='/report')
app.register_blueprint(usersService, url_prefix='/users')
# app.register_blueprint(reports)
# return app
