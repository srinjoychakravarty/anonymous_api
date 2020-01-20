class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
