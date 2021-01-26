from app import db
from flask import Response
from flask import request
# from flask_sqlalchemy import update
from app.utilities.handle_error import handle_error, handle_sql_error
from sqlalchemy.exc import SQLAlchemyError
from app.master.segmap.model import Segmap, SegmapSchema
from app.master.segmap.validate import validate_update
from app.master import masterService
import json
import logging

logger = logging.getLogger(__name__)

@masterService.route("/segmap/add", methods=['POST'])
def addSegmap():

    try:
        payload = request.json
        segmap = Segmap(**payload)
        # print(segmap)
        db.session.add(segmap)
        db.session.commit()

        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/segmap/list", methods=['POST'])
def listSegmap():

    try:        
        # payload = request.json
        itr = Segmap.query.all()   #filter_by(**payload)
        data = SegmapSchema(many=True, exclude=['secretKey', 'accessKey']).dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/segmap/update/<id>", methods=['POST'])
def editSegmap(id):

    try:
        payload = request.json
        payload = validate_update(payload)
        segmap = Segmap(**payload)
        db.session.merge(segmap)
        db.session.commit()
        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/segmap/get/<id>", methods=['POST'])
def getSegmap(id):

    try:
        itr = db.session.query(Segmap).get(id)
        data = SegmapSchema(exclude=['secretKey', 'accessKey']).dump(itr)
        resp = Response(json.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@masterService.route("/segmap/search", methods=['POST'])
def searchSegmapList():
    
    try:
        payload = request.json
        print(payload)
        itr = db.session.execute("call searchSegmap (:cid, :segid, :str, :type )", {'cid': payload['cid'], 'segid': payload['segid'], 'str': payload['str'], 'type': payload['type']})
        data = [dict(row) for row in itr]  
        resp = Response(json.dumps(data, default=str), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)

