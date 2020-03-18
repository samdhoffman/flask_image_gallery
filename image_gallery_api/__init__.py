# __init__.py tells python this is a package and initializes/ties together 
# what our app needs to run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # allows us to use diff DBs without changing our python code
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

# Init marshmallow
ma = Marshmallow(app)

# setup sqlalchemy db uri
# make sure that we can locate db file in the current dir
basedir = os.path.abspath(os.path.dirname(__file__))

# Database --> will look for file db.sqlite in the current folder we are in
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

# have to import below app and db declaration to avoid circular imports
from image_gallery_api import routes