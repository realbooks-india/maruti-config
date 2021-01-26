from app import db
from app import ma
from datetime import datetime


class Ledgermap (db.Model):
    __tablename__ = 'ledger_map'
    id = db.Column(db.String(50), primary_key=True, nullable=False)
    parent_group = db.Column(db.String(150))
    ledger_type = db.Column(db.String(60))
    dms_id = db.Column(db.String(45))
    dms_name = db.Column(db.String(400))
    dms_pan = db.Column(db.String(45))
    dms_gstin = db.Column(db.String(45))
    rlb_id = db.Column(db.String(45))
    rlb_name = db.Column(db.String(400))
    rlb_pan = db.Column(db.String(45))
    rlb_gstin = db.Column(db.String(45))
    status = db.Column(db.String(5))
    cid = db.Column(db.String(45))
    segid = db.Column(db.String(45))
    dt_create = db.Column(db.DateTime, default=datetime.utcnow)
    dt_update = db.Column(db.DateTime, default=datetime.utcnow)
    uid_create = db.Column(db.String(50))
    uid_update = db.Column(db.String(50))


class LedgermapSchema(ma.ModelSchema):
    class Meta:
        model = Ledgermap
