from app import db
from flask import Response
from flask import request
# from flask_sqlalchemy import update
from app.utilities.handle_error import handle_error, handle_sql_error
from sqlalchemy.exc import SQLAlchemyError
from app.master.itemmap.model import Itemmap, ItemmapSchema
from app.master.itemmap.validate import validate_update
from app.master import masterService
import json
import logging

logger = logging.getLogger(__name__)


@masterService.route("/itemmap/add", methods=['POST'])
def addItemmap():

    try:
        payload = request.json
        itemmap = Itemmap(**payload)
        # print(itemmap)
        db.session.add(itemmap)
        db.session.commit()

        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/itemmap/list", methods=['POST'])
def listItemmap():

    try:        
        # payload = request.json
        itr = Itemmap.query.all()   #filter_by(**payload)
        data = ItemmapSchema(many=True).dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/itemmap/update/<id>", methods=['POST'])
def editItemmap(id):

    try:
        payload = request.json
        payload = validate_update(payload)
        itemmap = Itemmap(**payload)
        db.session.merge(itemmap)
        db.session.commit()
        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/itemmap/get/<id>", methods=['POST'])
def getItemmap(id):

    try:
        itr = db.session.query(Itemmap).get(id)
        data = ItemmapSchema().dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)



