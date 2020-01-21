from sqlalchemy import MetaData, Table, Column, String, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

class Database():
    # replaces the user, password, hostname and database according to your configuration according to your information
    # engine = db.create_engine('postgresql://user:password@hostname/database_name')
    engine = db.create_engine('postgresql://postgres:postgres@127.0.0.1/postgres')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetch_by_query(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data)

    def fetch_user_by_name(self):
        meta = MetaData()
        user_from_table = Table('users', meta, Column('id'), Column('first_name'), Column('last_name'), Column('password'), Column('email_address'), Column('account_created'), Column('account_updated'))
        data = self.connection.execute(user_from_table.select())
        for user in data:
            print(user)

    def fetch_all_users(self):
        # bind an individual Session to the connection
        session = Session(bind = self.connection)
        users = session.query(User).all()
        for cust in users:
            print(cust)
        session.commit()

    def save_data(self, user):
        self.connection.execute(f"""INSERT INTO public.users (id, first_name, last_name, password, email_address, account_created, account_updated) VALUES ('{user.id}', '{user.first_name}', '{user.last_name}', '{user.password}', '{user.email_address}', '{user.account_created}', '{user.account_updated}')""")

    def update_user(self, email, new_password):
            session = Session(bind = self.connection)
            data_to_update = {User.password: new_password}
            user_data = session.query(User).filter(User.email_address == email)
            user_data.update(data_to_update)
            session.commit()

    def delete_user(self, pwd):
        session = Session(bind = self.connection)
        user_data = session.query(User).filter(User.password == pwd).first()
        session.delete(user_data)
        session.commit()

Base = declarative_base()

class User(Base):
    """Model for user account"""
    __tablename__ = 'users'
    id = Column(String, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    email_address = Column(String)
    account_created = Column(String)
    account_updated = Column(String)
    def __repr__(self):
        return "<User(id = '%s', first_name = '%s', last_name = '%s', password = '%s', email_address = '%s', account_created = '%s', account_updated = '%s')>" % (self.id, self.first_name, self.last_name, self.password, self.email_address, self.account_created, self.account_updated)
