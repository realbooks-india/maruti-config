
from flask import Response
from sqlalchemy.exc import SQLAlchemyError
import json 
import logging
import traceback

errorLogger = logging.getLogger('gunicorn.error')


def handle_sql_error(error, logger):
    error_message = str(error.__dict__['orig'])
    resp = {
        'error_code' : '101',
        'error_type' : 'SqlError',
        'error_message': error_message
    }
    logger.error(json.dumps(resp))
    errorLogger.error(error, exc_info=1)
    return Response(json.dumps(resp), status=400, mimetype='application/json')


def handle_error(error, logger):
    if type(error).__name__=='TypeError':
        resp = {
            'error_code' : '102',
            'error_type' : 'TypeError',
            'error_message': str(error)
        }
        logger.error(json.dumps(resp))
        errorLogger.error(error, exc_info=1)
        return Response(json.dumps(resp), status=400, mimetype='application/json')

    else: 
        resp = {
            'error_code' : '999',
            'error_message': str(error)
        }
        logger.error(json.dumps(resp))
        errorLogger.error(error, exc_info=1)

        return Response(json.dumps(resp), status=400, mimetype='application/json')
