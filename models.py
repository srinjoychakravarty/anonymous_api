from datetime import datetime
from config import sql_alchemy_db, marshmallow

class User(sql_alchemy_db.Model):
    __tablename__ = 'user'
    user_id = sql_alchemy_db.Column(sql_alchemy_db.Integer, primary_key=True)
    lname = sql_alchemy_db.Column(sql_alchemy_db.String(32), index=True)
    fname = sql_alchemy_db.Column(sql_alchemy_db.String(32))
    timestamp = sql_alchemy_db.Column(sql_alchemy_db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserSchema(marshmallow.ModelSchema):
    class Meta:
        model = User
        sqla_session = sql_alchemy_db.session
