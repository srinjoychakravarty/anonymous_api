import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connexion_application = connexion.App(__name__, specification_dir = basedir)

# Get the underlying Flask app instance
flask_application = connexion_application.app

# Configure the SQLAlchemy part of the app instance
flask_application.config['SQLALCHEMY_ECHO'] = True
flask_application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')
# flask_application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'
flask_application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
sql_alchemy_db = SQLAlchemy(flask_application)

# Initialize Marshmallow
marshmallow = Marshmallow(flask_application)
