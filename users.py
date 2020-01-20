"""
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

def read_one(lname):
    """
    This function responds to a request for /v1/users/{lname}
    with one matching user from users
    :param lname:   last name of user to find
    :return:        user matching last name
    """
    if lname in USERS:                                                          # Does the user exist in users?
        user = USERS.get(lname)
    else:                                                                       # otherwise, nope, not found
        abort(
            404, "User with last name {lname} not found".format(lname=lname)
        )
    return user

def create(user):
    """
    This function creates a new user in the users structure
    based on the passed in user data
    :param user:  user to create in users structure
    :return:        201 on success, 406 on user exists
    """
    lname = user.get("lname", None)
    fname = user.get("fname", None)
    if lname not in USERS and lname is not None:                                # Does the user exist already?
        USERS[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    else:                                                                       # Otherwise, they exist, that's an error
        abort(
            406,
            "User with last name {lname} already exists".format(lname=lname),
        )

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
