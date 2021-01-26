import requests
import pytest
import json


def test_updatedSegmap(url, payload, headers, monkeypatch):
    url = url['updateSegmap'] + payload['id']
    payload['parent_group'] = "Segmap-2"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200


def test_updateSegmap_wrongDataType(url, payload, headers, monkeypatch):
    url = url['updateSegmap'] + payload['id']
    monkeypatch.setitem(payload,'dt_update','abc') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


def test_updateSegmap_withExtraField(url, payload, headers, monkeypatch):
    url = url['updateSegmap'] + payload['id']
    monkeypatch.setitem(payload,'extra_field','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


# def test_updateSegmap_no_token (url, payload, headers, monkeypatch):
#     url = url['updateSegmap'] + payload['id']
#     monkeypatch.setitem(headers,'Authorization','') 
#     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
#     assert response.status_code == 401
