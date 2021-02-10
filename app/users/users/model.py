from app import db
from app import ma
from datetime import datetime


class Users (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    is_client = db.Column(db.Integer)
    client_id = db.Column(db.String(50))
    status = db.Column(db.Integer)
    segid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    visible = db.Column(db.Integer)
    txnid = db.Column(db.String(50))
    version = db.Column(db.String(50))
    dt_create = db.Column(db.DateTime, default=datetime.utcnow)
    dt_update = db.Column(db.DateTime, default=datetime.utcnow)
    uid_create = db.Column(db.String(50))
    uid_update = db.Column(db.String(50))


    __mapper_args__ = {
        "version_id_col": version
    }


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users
