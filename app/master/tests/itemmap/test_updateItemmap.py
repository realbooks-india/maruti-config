import requests
import pytest
import json


def test_updatedItemmap(url, payload, headers, monkeypatch):
    url = url['updateItemmap'] + payload['id']
    payload['parent_group'] = "Itemmap-2"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200


def test_updateItemmap_wrongDataType(url, payload, headers, monkeypatch):
    url = url['updateItemmap'] + payload['id']
    monkeypatch.setitem(payload,'dt_update','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


def test_updateItemmap_withExtraField(url, payload, headers, monkeypatch):
    url = url['updateItemmap'] + payload['id']
    monkeypatch.setitem(payload,'extra_field','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


# def test_updateItemmap_no_token (url, payload, headers, monkeypatch):
#     url = url['updateItemmap'] + payload['id']
#     monkeypatch.setitem(headers,'Authorization','') 
#     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
#     assert response.status_code == 401
