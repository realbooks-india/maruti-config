import pytest
import uuid

@pytest.fixture(scope="package")
def payload():
    id = uuid.uuid4()
    data = {
    'id' : str(id),
    'parent_group' : "",
    'mul_dealer_cd' : "",
    'outlet_cd' : "",
    'loc_cd' : "",
    'dealer_for_cd' : "",
    'seg_ledger' : "",
    'cost_center' : "",
    'godown' : "",
    'secretKey' : "",
    'accessKey' : "",
    'emailid' : "",
    'accountName' : "",
    'companyGstin' : "",
    'status' : "",
    'cid' : 0,
    'segid' : 0,
    'visible' : 0,
    'dt_create' : '2020-03-28 23:11:06', #2020-03-28
    'dt_update' : '2020-03-28 23:11:06', #2020-03-28
    'uid_create' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    'uid_update' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    }
    return data


@pytest.fixture(scope="package")
def url(baseurl):
    urls = { 
        'addSegmap': baseurl + "/master/segmap/add", 
        'updateSegmap': baseurl + "/master/segmap/update/", 
        'getSegmap': baseurl + "/master/segmap/get/", 
        'listSegmap': baseurl + "/master/segmap/list", 
        }
    return urls
