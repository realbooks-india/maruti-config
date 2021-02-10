from boto3.dynamodb.conditions import Key, Attr
from app.report import reportService
from app import dynamodb, rd
from flask import Response
from flask import request
from datetime import datetime
from flask_jwt_extended import jwt_required
import requests as req
import json


@reportService.route("/maruti-sync/<account>/<dt>", methods=['GET'])
def listTxnStatus(account, dt):

    try:
        table = dynamodb.Table('Maruti-DMS-Txns')
        result = table.query(
                    IndexName='account-dt-index',
                    KeyConditionExpression=Key('account').eq(account) & Key('dt').eq(dt)
                )
        resp = Response(json.dumps(result['Items'], default=str), status=200, mimetype='application/json')
        print("From maruti sync")
        result.pop("Items")
        print(result)
        return resp
    except Exception as e: 
        print("Error", e)
        return "Error"


@reportService.route("/maruti-sync-repost/<id>", methods=['GET'])
# @jwt_required
def repostTxn(id):

    try:
        res = rd.publish('maruti-dms::manual-post',json.dumps({"id" : id}))
        print(res)
        return "Done"

    except Exception as e: 
        print("Error", e)
        return "Error"

