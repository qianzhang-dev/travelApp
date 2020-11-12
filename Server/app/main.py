from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

from .config import ConfigProvider 

app: Flask = Flask(__name__)
ConfigProvider.apply_to_app(app)

db: SQLAlchemy = SQLAlchemy(app)
migrate: Migrate = Migrate(app, db)
api: Api = Api(app)

from . import models
from . import apis

api.add_resource(apis.Index, '/')