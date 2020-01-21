import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))
connexion_application = connexion.App(__name__, specification_dir = basedir)    # Create the Connexion application instance
flask_application = connexion_application.app                                   # Get the underlying Flask app instance
flask_application.config['SQLALCHEMY_ECHO'] = True                              # Configure the SQLAlchemy part of the app instance
# sqlite_url = "sqlite:////" + os.path.join(basedir, "users.db")                  # Build the Sqlite ULR for SqlAlchemy
#flask_application.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
#flask_application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'




postgresql_url = 'postgres+psycopg2://postgres:postgres@127.0.0.1:5050/postgres'
flask_application.config['SQLALCHEMY_DATABASE_URI'] = postgresql_url
# flask_application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'
flask_application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sql_alchemy_db = SQLAlchemy(flask_application)                                  # Create the SQLAlchemy db instance
marshmallow = Marshmallow(flask_application)                                    # Initialize Marshmallow
