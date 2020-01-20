import os
from config import sql_alchemy_db
from models import User

USERS = [                                                                       # Data to seed database with
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'}
]
if (os.path.exists('users.db')):                                                # Delete database file if it exists currently
    os.remove('users.db')
sql_alchemy_db.create_all()                                                     # Create the database
for user in USERS:                                                              # Iterate over the USERS structure and populate the database
    usr = User(lname=user['lname'], fname=user['fname'])
    sql_alchemy_db.session.add(usr)
sql_alchemy_db.session.commit()
