from datetime import datetime                                                   # 3rd party modules
# from config import sql_alchemy_db, marshmallow

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key = True)
    lastname = Column(String)
    firstname = Column(String)
    email = Column(String)
    password = Column(String)
    timestamp = Column(Date)

    def __repr__(self):
        return "<User(lastname = '{}', firstname = '{}', email = '{}', password = '{}', timestamp = '{}')>".format(self.lastname, self.firstname, self.email, self.password, self.timestamp)

# class UserSchema(marshmallow.ModelSchema):
#     class Meta:
#         model = User
#         sqla_session = sql_alchemy_db.session

postgresql_url = 'postgres+psycopg2://postgres:postgres@127.0.0.1:5050/postgres'
engine = create_engine(postgresql_url)
Base.metadata.create_all(engine)

# class User(sql_alchemy_db.Model):
#     __tablename__ = 'user'
#     user_id = sql_alchemy_db.Column(sql_alchemy_db.Integer, primary_key = True)
#     lname = sql_alchemy_db.Column(sql_alchemy_db.String(32))
#     fname = sql_alchemy_db.Column(sql_alchemy_db.String(32))
#     timestamp = sql_alchemy_db.Column(sql_alchemy_db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
#
# class UserSchema(marshmallow.ModelSchema):
#     class Meta:
#         model = User
#         sqla_session = sql_alchemy_db.session
