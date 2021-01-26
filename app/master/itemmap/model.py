from app import db
from app import ma
from datetime import datetime


class Itemmap (db.Model):
    __tablename__ = 'item_map'
    id = db.Column(db.String(45), primary_key=True, nullable=False)
    parent_group = db.Column(db.String(45))
    dms_id = db.Column(db.String(45))
    rlb_item_code = db.Column(db.String(45))
    rlb_item_name = db.Column(db.String(250))
    uom = db.Column(db.String(45))
    rlb_item_group = db.Column(db.String(45))
    segid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    status = db.Column(db.Integer)
    uid_create = db.Column(db.String(45))
    uid_update = db.Column(db.String(45))
    dt_create = db.Column(db.DateTime, default=datetime.utcnow)
    dt_update = db.Column(db.DateTime, default=datetime.utcnow)


class ItemmapSchema(ma.ModelSchema):
    class Meta:
        model = Itemmap
