import pytest
import uuid


@pytest.fixture(scope="package")
def payload():
    id = uuid.uuid4()
    data = {
        'id' : str(id),
        'name' : "User-" + str(id),
        'mobile' : "9831414000",
        'email' : "Pending",
        'password' : "Pswd-1",
        'status' : "1",
        'segid' : -1,
        'cid' : -1,
        'txnid' : "aa52ffaa-8048-4a6f-960e-ba79c985b096",
        'dt_create' : '2020-03-28 23:11:06', #2020-03-28
        'dt_update' : '2020-03-28 23:11:06', #2020-03-28
        'uid_create' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
        'uid_update' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
        }
    return data


@pytest.fixture(scope="package")
def url(baseurl):
    urls = { 
        'addUsers': baseurl + "/users/add", 
        'updateUsers': baseurl + "/users/update/", 
        'getUsers': baseurl + "/users/get/", 
        'listUsers': baseurl + "/users/list", 
        'login': baseurl + '/users/login'
        }
    return urls
