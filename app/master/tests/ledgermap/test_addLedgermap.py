import requests
import pytest
import json


def test_addLedgermap_wrongDataType(url, payload, headers, monkeypatch):
    monkeypatch.setitem(payload,'dt_create','') 
    response = requests.request("POST", url['addLedgermap'], data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


def test_addLedgermap_withExtraField(url, payload, headers, monkeypatch):
    monkeypatch.setitem(payload,'extra_field','') 
    response = requests.request("POST", url['addLedgermap'], data=json.dumps(payload), headers=headers)
    assert response.status_code == 400


# def test_addLedgermap_no_token (url, payload, headers, monkeypatch):
#     monkeypatch.setitem(headers,'Authorization','') 
#     response = requests.request("POST", url['addLedgermap'], data=json.dumps(payload), headers=headers)
#     assert response.status_code == 401


#make sure to start function name with test
def test_addLedgermap(url, payload, headers, monkeypatch):
    response = requests.request("POST", url['addLedgermap'], data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200
