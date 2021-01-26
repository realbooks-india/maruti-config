from app import db
from flask import Response
from flask import request
# from flask_sqlalchemy import update
from app.utilities.handle_error import handle_error, handle_sql_error
from sqlalchemy.exc import SQLAlchemyError
from app.master.ledgermap.model import Ledgermap, LedgermapSchema
from app.master.ledgermap.validate import validate_update
from app.master import masterService
import json
import logging

logger = logging.getLogger(__name__)


@masterService.route("/ledgermap/add", methods=['POST'])
def addLedgermap():

    try:
        payload = request.json
        ledgermap = Ledgermap(**payload)
        # print(ledgermap)
        db.session.add(ledgermap)
        db.session.commit()

        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/ledgermap/list", methods=['POST'])
def listLedgermap():

    try:        
        # payload = request.json
        itr = Ledgermap.query.all()   #filter_by(**payload)
        data = LedgermapSchema(many=True).dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/ledgermap/update/<id>", methods=['POST'])
def editLedgermap(id):

    try:
        payload = request.json
        payload = validate_update(payload)
        ledgermap = Ledgermap(**payload)
        db.session.merge(ledgermap)
        db.session.commit()
        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/ledgermap/get/<id>", methods=['POST'])
def getLedgermap(id):

    try:
        itr = db.session.query(Ledgermap).get(id)
        data = LedgermapSchema().dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)



