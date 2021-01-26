import requests
import pytest
import json


def test_updatedLedgermap(url, payload, headers, monkeypatch):
    url = url['updateLedgermap'] + payload['id']
    payload['parent_group'] = "Ledgermap-2"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200


def test_updateLedgermap_wrongDataType(url, payload, headers, monkeypatch):
    url = url['updateLedgermap'] + payload['id']
    monkeypatch.setitem(payload,'dt_create','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


def test_updateLedgermap_withExtraField(url, payload, headers, monkeypatch):
    url = url['updateLedgermap'] + payload['id']
    monkeypatch.setitem(payload,'extra_field','') 
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


# def test_updateLedgermap_no_token (url, payload, headers, monkeypatch):
#     url = url['updateLedgermap'] + payload['id']
#     monkeypatch.setitem(headers,'Authorization','') 
#     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
#     assert response.status_code == 401
