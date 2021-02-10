import requests
import pytest
import json


#make sure to start function name with test
def test_login_wrong_user (url, payload, headers):
    response = requests.post(url['login'], auth=('null', 'null'))
    assert response.status_code == 401


def test_login_no_pswd (url, payload, headers):
    response = requests.post(url['login'], auth=('test', ''))
    assert response.status_code == 401


# def test_first_login_invalid_after_second_login (url, payload, headers, monkeypatch):

#     #  first login
#     resp = requests.post(url['login'], auth=('test-2', 'Pswd-1'))
#     data = resp.json()
#     monkeypatch.setitem(headers,'x-access-token',data['token']) 

#     # second login with same user
#     resp = requests.post(url['login'], auth=('test-2', 'Pswd-1'))
#     response = requests.post(url['listUsers'], data=json.dumps(payload), headers=headers)

#     # Test first login
#     if response.status_code != 401:
#         print(response.json())
#     assert response.status_code == 401


