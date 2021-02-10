# from app import app, rd
from functools import wraps
from flask import g, Response
import jwt
import os
import re

def validate_token(f, logger):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        print(request.get_json())
        print(request.headers)

        if 'x-access-token' in request.headers:
            print(request.headers['x-access-token'])
            token = request.headers['x-access-token']
            
        # Exit - if token does not exist
        if not token:
            logger.warning('Token is missing!')
            Response({'message' : 'Token is missing!'}, status=401, mimetype='application/json')

        try: # Entry Point - validating the token
            
            key_file = os.path.join(os.path.dirname(app.instance_path), 'task_rsa.pub')
            public_key = open(key_file).read()
            data = jwt.decode(token, public_key, algorithm='RS256')
            logger.info('Token is valid for  uid %s', data['uid'])

            # Exit - if the User is not logged in
            if rd.exists(data['uid']) == 0:
                logger.warning('User may have logged out. Key is not existing in Redis for uid %s', data['uid'])
                Response({'message' : 'You seem to have logged out. Please login!'}, status=401, mimetype='application/json')


            # Exit - if the session id does not exist - prevent a second login
            if data['sessionid'] != rd.hget(data['uid'],'sessionid'):
                logger.warning('Token is overwritten for uid %s', data['uid'])
                Response({'message' : 'Token is invalidated by another login !'}, status=401, mimetype='application/json')

            # Setting variables in Flask-g
            g.uid = data['uid']
            g.segid = int(rd.hget(data['uid'], 'segid'))
            g.cid = int(rd.hget(data['uid'], 'cid'))
            g.sessionid = rd.hget(data['uid'], 'sessionid')
            logger.info('User is authorised for uid %s with sessionid %s', data['uid'], data['sessionid'])

        except:
            # Exit - if token could not be validated
            logger.warning('Token is invalid!')
            Response({'message' : 'Token is invalid!'}, status=401, mimetype='application/json')

        logger.info('login page accessed')
        return f(*args, **kwargs)
    return decorated_function



def validate_request(request, logger):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        # Checking for proper JSON Format
        if not isinstance(request.json,dict):
            logger.warning('JSON object not endoded properly for user %s, for session %s', g.uid, g.sessionid)
            Response({'message' : "JSON object not endoded properly"}, status=401, mimetype='application/json')

        # Checking for CID key
        # url_match = re.search('\/users$|\/users\/', request.path)
        # if not url_match :
        if not 'cid' in request.json:
            logger.warning('cid key is missing in JSON for user %s, for session %s', g.uid, g.sessionid)
            Response({'message' : "cid key is missing in JSON"}, status=401, mimetype='application/json')

        # Checking for CID
        if g.cid != request.json['cid']:
            logger.warning('requsted cid not matching with redis for user %s, for session %s', g.uid, g.sessionid)
            Response({'message' : "requsted cid not matching with cid selected in server"}, status=401, mimetype='application/json')

        logger.info('request is valid for user %s, for session %s', g.uid, g.sessionid)
        return f(*args, **kwargs)

    return decorated_function


