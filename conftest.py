# settings.py
import pytest
from typing import Dict, Tuple
import requests


@pytest.fixture(scope='session')
def headers(baseurl):
    # resp = requests.post( baseurl + "/users/login", auth=('test-1', 'Pswd-1'))
    # data = resp.json()
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "localhost:8080",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "127",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        # 'Authorization': 'Bearer ' + data['token'],
        # 'ls-uid': data['uid']
    }
    return headers


@pytest.fixture(scope="session")
def baseurl():
    return  "http://localhost:8080"

