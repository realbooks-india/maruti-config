from app import db
from app import ma
from datetime import datetime


class Segmap (db.Model):
    __tablename__ = 'seg_map'
    id = db.Column(db.String(50), primary_key=True, nullable=False)
    parent_group = db.Column(db.String(200))
    mul_dealer_cd = db.Column(db.String(45))
    outlet_cd = db.Column(db.String(45))
    loc_cd = db.Column(db.String(45))
    dealer_for_cd = db.Column(db.String(45))
    seg_ledger = db.Column(db.String(200))
    cost_center = db.Column(db.String(200))
    godown = db.Column(db.String(100))
    secretKey = db.Column(db.String(100))
    accessKey = db.Column(db.String(100))
    emailid = db.Column(db.String(150))
    accountName = db.Column(db.String(45))
    companyGstin = db.Column(db.String(45))
    status = db.Column(db.String(45))
    cid = db.Column(db.Integer)
    segid = db.Column(db.Integer)
    visible = db.Column(db.Integer)
    dt_create = db.Column(db.DateTime, default=datetime.utcnow)
    dt_update = db.Column(db.DateTime, default=datetime.utcnow)
    uid_create = db.Column(db.String(50))
    uid_update = db.Column(db.String(50))


class SegmapSchema(ma.ModelSchema):
    class Meta:
        model = Segmap
