import sqlalchemy as db

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    # engine = db.create_engine('postgresql://user:password@hostname/database_name')
    engine = db.create_engine('postgresql://postgres:postgres@127.0.0.1/postgres')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

        self.connection.close()

    def saveData(self, user):
        self.connection.execute(f"""INSERT INTO public.user (email, password, firstname, lastname) VALUES ('{user.email}', '{user.password}', '{user.firstname}', '{user.lastname}')""")


class User():
    def __init__(self, email, password, firstname, lastname):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
