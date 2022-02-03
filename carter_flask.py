import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.base")

# Base db class
db = SQLAlchemy(app)

migrate = Migrate(app, db)