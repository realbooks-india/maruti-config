import requests
import pytest
import json


def test_getUsers(url, payload, headers):
    url = url['getUsers'] + payload['id']
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json()) 
    assert response.status_code == 200


def test_getUsers_no_token (url, payload, headers, monkeypatch):
    url = url['getUsers'] + payload['id']
    monkeypatch.setitem(headers,'Authorization','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 401
