def read_one(person_id):

    """

    This function responds to a request for /api/people/{person_id}

    with one matching person from people


    :param person_id:   ID of person to find

    :return:            person matching ID

    """

    # Get the person requested

    person = Person.query \

        .filter(Person.person_id == person_id) \

        .one_or_none()


    # Did we find a person?

    if person is not None:


        # Serialize the data for the response

        person_schema = PersonSchema()

        return person_schema.dump(person).data


    # Otherwise, nope, didn't find that person

    else:

        abort(404, 'Person not found for Id: {person_id}'.format(person_id=person_id))
