from sqlalchemy import create_engine
# from models import Base

postgresql_url = 'postgres+psycopg2://postgres:postgres@127.0.0.1:5050/postgres'
engine = create_engine(postgresql_url)
Base.metadata.create_all(engine)
