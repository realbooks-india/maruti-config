from app import db
from flask import Response, request, jsonify
from app.utilities.handle_error import handle_error, handle_sql_error
from sqlalchemy.exc import SQLAlchemyError
from app.users.users.model import Users, UsersSchema
from app.users.users.validate import validate_update
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required
from app.users import usersService
import simplejson
import json
import logging
import bcrypt

logger = logging.getLogger(__name__)


@usersService.route("/add", methods=['POST'])
@jwt_required
def addUsers():

    try:
        payload = request.json
        users = Users(**payload)
        print(users)
        # hashed_password = generate_password_hash(users.password, method='sha256')
        hashed_password = hashed = bcrypt.hashpw(users.password.encode("utf-8"), bcrypt.gensalt())
        users.password = hashed_password
        db.session.add(users)
        db.session.commit()
        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@usersService.route("/list", methods=['POST'])
@jwt_required
def listUsers():

    try:
        # payload = request.json
        itr = Users.query.all()   #filter_by(**payload)
        data = UsersSchema(many=True).dumps(itr)
        resp = Response(simplejson.dumps(data), status=200, mimetype='application/json')
        return resp
        
    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@usersService.route("/update/<id>", methods=['POST'])
@jwt_required
def editUsers(id):

    try:
        payload = request.json
        payload = validate_update(payload)
        users = Users(**payload)
        db.session.merge(users)
        db.session.commit()
        resp = Response("Success", status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


@usersService.route("/get/<id>", methods=['POST'])
@jwt_required
def getUsers(id):

    try:
        itr = db.session.query(Users).get(id)
        data = UsersSchema().dumps(itr)
        resp = Response(simplejson.dumps(data), status=200, mimetype='application/json')
        return resp

    except SQLAlchemyError as e:
        return handle_sql_error(e, logger)

    except Exception as e:
        return handle_error(e, logger)


