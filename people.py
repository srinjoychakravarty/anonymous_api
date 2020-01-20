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
