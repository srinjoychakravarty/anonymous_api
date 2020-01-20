USERimport os
from config import sql_alchemy_db
from models import User

# Data to initialize database with
USERS = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'}
]

# Delete database file if it exists currently
if os.path.exists('users.db'):
    os.remove('users.db')

# Create the database
sql_alchemy_db.create_all()

# Iterate over the USERS structure and populate the database
for user in USERS:
    p = User(lname=user['lname'], fname=user['fname'])
    sql_alchemy_db.session.add(p)
sql_alchemy_db.session.commit()
