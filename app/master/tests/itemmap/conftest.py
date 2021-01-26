import pytest
import uuid

@pytest.fixture(scope="package")
def payload():
    id = uuid.uuid4()
    data = {
    'id' : str(id),
    'parent_group' : "",
    'dms_id' : "",
    'rlb_item_code' : "",
    'rlb_item_name' : "",
    'uom' : "",
    'rlb_item_group' : "",
    'segid' : 1,
    'cid' : 1,
    'status' : 1,
    'dt_create' : '2021-01-10 23:11:06', #2020-03-28
    'dt_update' : '2021-01-10 23:11:06', #2020-03-28
    'uid_create' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    'uid_update' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    }
    return data


@pytest.fixture(scope="package")
def url(baseurl):
    urls = { 
        'addItemmap': baseurl + "/master/itemmap/add", 
        'updateItemmap': baseurl + "/master/itemmap/update/", 
        'getItemmap': baseurl + "/master/itemmap/get/", 
        'listItemmap': baseurl + "/master/itemmap/list", 
        }
    return urls
