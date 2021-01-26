import requests
import pytest
import json


#make sure to start function name with test
def test_listLedgermap(url, payload, headers, monkeypatch):
    response = requests.request("POST", url['listLedgermap'], data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print(response.json())
    assert response.status_code == 200


# def test_listLedgermap_no_token (url, payload, headers, monkeypatch):
#     monkeypatch.setitem(headers,'Authorization','') 
#     response = requests.request("POST", url['listLedgermap'], data=json.dumps(payload), headers=headers)
#     assert response.status_code == 401


# def test_wrong_json_encoding (url, payload, headers, monkeypatch):
#     response = requests.request("POST", url['listLedgermap'], data=payload, headers=headers)
#     # Test first login
#     if response.status_code != 400:
#         print(response.json())
#     assert response.status_code == 400

    
# def test_payload_with_no_cid (url, payload, headers, monkeypatch):
#     monkeypatch.delitem(payload, 'cid')
#     response = requests.request("POST", url['listLedgermap'], data=json.dumps(payload), headers=headers)
#     # Test first login
#     if response.status_code != 400:
#         print(response.json())
#     assert response.status_code == 400


# def test_wrong_cid (url, payload, headers, monkeypatch):
#     monkeypatch.setitem(payload,'cid',-2) 
#     response = requests.request("POST", url['listLedgermap'], data=json.dumps(payload), headers=headers)
#     # Test first login
#     if response.status_code != 400:
#         print(response.json())
#     assert response.status_code == 400