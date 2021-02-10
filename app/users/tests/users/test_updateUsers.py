import requests
import pytest
import json
import uuid


def test_updatedUsers(url, payload, headers):
    url = url['updateUsers'] + payload['id']
    payload['group'] = "Group-2"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200


def test_updateUsers_wrongDataType(url, payload, headers, monkeypatch):
    url = url['updateUsers'] + payload['id']
    monkeypatch.setitem(payload,'dt_create','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


def test_updateUsers_withExtraField(url, payload, headers, monkeypatch):
    url = url['updateUsers'] + payload['id']
    monkeypatch.setitem(payload,'extra_field','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.text)
    assert response.status_code == 400


def test_updateUsers_no_token (url, payload, headers, monkeypatch):
    url = url['updateUsers'] + payload['id']
    monkeypatch.setitem(headers,'Authorization','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 401

