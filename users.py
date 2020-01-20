"""
This is the users module and supports all the REST actions for the
USERS collection
"""
from config import sql_alchemy_db                                               # System modules
from flask import make_response, abort
from models import User, UserSchema

def read_all():
    """
    This function responds to a request for /v1/users
    with the complete list of users
    :return:        json string of list of users
    """
    users = User.query.order_by(User.lname).all()                               # Create the list of users from our data
    print("THIS IS THE USER LIST: " + str(users))
    user_schema = UserSchema(many = True)                                       # Serialize the data for the response
    serialized_data = user_schema.dump(users)
    print("ALL DATA SERIALIZED: " + str(serialized_data))
    return serialized_data

def read_one(user_id):
    """
    This function responds to a request for /v1/users/{user_id}
    with one matching user from users
    :param user_id:     id of user to find
    :return:            user matching id
    """
    user = User.query.filter(User.user_id == user_id).one_or_none()             # Get the user requested
    if user is not None:                                                        # Did we find a user?
        user_schema = UserSchema()                                              # Serialize the data for the response
        serialized_data = user_schema.dump(user)
        return serialized_data
    else:                                                                       # Otherwise, nope, didn't find that user
        abort(404, 'User not found for Id: {user_id}'.format(user_id = user_id))

def create(user):
    """
    This function creates a new user in the users structure
    based on the passed-in user data
    :param user:    user to create in users structure
    :return:        201 on success, 409 on user exists
    """
    fname = user.get('fname')
    lname = user.get('lname')
    existing_user = User.query.filter(User.fname == fname).filter(User.lname == lname).one_or_none()
    if existing_user is None:                                                   # Can we insert this user?
        schema = UserSchema()                                                   # Create a user instance using the schema and the passed-in user
        new_user = schema.load(user, session = sql_alchemy_db.session)
        sql_alchemy_db.session.add(new_user)                                    # Add the user to the database
        sql_alchemy_db.session.commit()
        serialized_data = schema.dump(new_user)                                 # Serialize and return the newly created user in the response
        return serialized_data, 201
    else:                                                                       # Otherwise, nope, user exists already
        abort(409, "User {firstname} {lastname} exists already".format(firstname = fname, lastname = lname))

def update(user_id, user):
    """
    This function updates an existing user in the users structure
    Throws an error if a user with the name we want to update to
    already exists in the database.
    :param user_id:   id of the user to update in the users structure
    :param user:      user to update
    :return:          updated user structure
    """
    update_user = User.query.filter(User.user_id == user_id).one_or_none()      # Get the user requested from the db into session
    fname = user.get("fname")                                                   # Try to find an existing user with the same name as the update
    lname = user.get("lname")
    existing_user = (User.query.filter(User.fname == fname).filter(User.lname == lname).one_or_none())
    if update_user is None:                                                     # Are we trying to find a user that does not exist?
        abort(404, "User not found for id: {user}".format(user = user_id))
    elif (existing_user is not None and existing_user.user_id != user_id):      # Would our update create a duplicate of another user already existing?
        abort(409, "User {firstname} {lastname} exists already".format(firstname = fname, lastname = lname))
    else:                                                                       # Otherwise go ahead and update!
        schema = UserSchema()                                                   # turn the passed in user into a db object
        update = schema.load(user, session = sql_alchemy_db.session)
        update.user_id = update_user.user_id                                    # Set the id to the user we want to update
        sql_alchemy_db.session.merge(update)                                    # merge the new object into the old and commit it to the db
        sql_alchemy_db.session.commit()
        serialized_data = schema.dump(update_user)                              # return updated user in the response
        return serialized_data, 200

def delete(user_id):
    """
    This function deletes a user from the users structure
    :param user_id:     id of the user to delete
    :return:            200 on successful delete, 404 if not found
    """
    user = User.query.filter(User.user_id == user_id).one_or_none()             # Get the user requested
    if user is not None:                                                        # Did we find a user?
        sql_alchemy_db.session.delete(user)
        sql_alchemy_db.session.commit()
        return make_response("User {user} deleted".format(user = user_id), 200)
    else:                                                                       # Otherwise, nope, didn't find that user
        abort(404, "User not found for id: {user}".format(user = user_id))
