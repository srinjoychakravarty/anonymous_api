user"""
This is the users module and supports all the REST actions for the
USERS collection
"""
from config import sql_alchemy_db                                               # System modules
from datetime import datetime                                                   # 3rd party modules
from flask import make_response, abort
from models import User, UserSchema

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

USERS = {                                                                       # Data to serve with our API
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    """
    This function responds to a request for /v1/users
    with the complete lists of users
    :return:        json string of list of users
    """
    users = User.query.order_by(User.lname).all()                               # Create the list of users from our data
    user_schema = UserSchema(many = True)                                       # Serialize the data for the response
    return user_schema.dump(users).data

def read_one(user_id):
    """
    This function responds to a request for /v1/users/{user_id}
    with one matching user from users
    :param user_id:   ID of user to find
    :return:            user matching ID
    """
    user = User.query.filter(User.user_id == user_id).one_or_none()             # Get the user requested
    if user is not None:                                                        # Did we find a user?
        user_schema = UserSchema()                                              # Serialize the data for the response
        return user_schema.dump(user).data                                      # Otherwise, nope, didn't find that user
    else:
        abort(404, 'User not found for Id: {user_id}'.format(user_id = user_id))

def create(user):
    """
    This function creates a new user in the people structure
    based on the passed-in user data
    :param user:  user to create in people structure
    :return:        201 on success, 406 on user exists
    """
    fname = user.get('fname')
    lname = user.get('lname')
    existing_user = User.query.filter(User.fname == fname).filter(User.lname == lname).one_or_none()
    if existing_user is None:                                                   # Can we insert this user?
        schema = UserSchema()                                                   # Create a user instance using the schema and the passed-in user
        new_user = schema.load(user, session=db.session).data
        db.session.add(new_user)                                                # Add the user to the database
        db.session.commit()
        return schema.dump(new_user).data, 201                                  # Serialize and return the newly created user in the response
    else:                                                                       # Otherwise, nope, user exists already
        abort(409, f'User {fname} {lname} exists already')

def update(lname, user):
    """
    This function updates an existing user in the users structure
    :param lname:   last name of user to update in the users structure
    :param user:  user to update
    :return:        updated user structure
    """
    if lname in USERS:                                                          # Does the user exist in users?
        USERS[lname]["fname"] = user.get("fname")
        USERS[lname]["timestamp"] = get_timestamp()
        return USERS[lname]
    else:                                                                       # otherwise, nope, that's an error
        abort(
            404, "User with last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    """
    This function deletes a user from the users structure
    :param lname:   last name of user to delete
    :return:        200 on successful delete, 404 if not found
    """
    if lname in USERS:                                                          # Does the user to delete exist?
        del USERS[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )
    else:                                                                       # Otherwise, nope, user to delete not found
        abort(
            404, "User with last name {lname} not found".format(lname=lname)
        )
