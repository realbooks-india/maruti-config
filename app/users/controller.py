from app import db, app, rd
from . import usersService
import datetime
from flask import Flask, request, jsonify, make_response
from werkzeug.security import check_password_hash
from app.utilities.authorise import validate_token, validate_request
from app.users.users.model import Users, UsersSchema
from flask_jwt_extended import create_access_token
import logging
import uuid
import bcrypt
import json


logger = logging.getLogger(__name__)

@usersService.before_request
def before_request():
    logger.info("Users Before request!")
    # Just use the query parameter "tenant"
    # db.choose_tenant('organisation') 
    # validate_token(request, logger)
    # validate_request(request, logger)


@usersService.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    
    if not auth:
        return jsonify('Authorization request missing'), 401

    if not auth.username:
        return jsonify('Username is missing'), 401

    if not auth.password:
        return jsonify('Password is missing'), 401

    user = Users.query.filter_by(email=auth.username).first()
    if not user:
        return jsonify('Username not found'), 401

    # if check_password_hash(user.password, auth.password):
    print(user.password)
    if bcrypt.checkpw(auth.password.encode('utf-8'), user.password.encode('utf-8') ):

        # generate session id
        sessionid = str(uuid.uuid4())
        print('sessionid at login:', sessionid, user.id)

        jwt_payload = {
            'uid' : user.id, 
            'cid' : user.cid,
            'sessionid' : sessionid, 
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=app.config['SESSION_EXPIRY'])
            }

        token = create_access_token(identity=user.id, headers=jwt_payload)

        # set session keys and setting expiry in redis
        # rd.hset(user.id,'token', token)
        rd.hset(user.id,'sessionid', sessionid)
        rd.expire(user.id, app.config['SESSION_EXPIRY'])

        # set additional keys in redis
        rd.hset(user.id,'segid', user.segid)
        rd.hset(user.id,'cid', user.cid)

        return jsonify({'token' : token})

    return jsonify('Invalid Password'), 401


@usersService.route("/")
def show():
    return {"Say":"Hi users"}
    # return render_template("index2.html")

