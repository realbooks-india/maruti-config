import pytest
import uuid

@pytest.fixture(scope="package")
def payload():
    id = str(uuid.uuid4())
    data = {
    'id' : id,
    'parent_group' : "",
    'ledger_type' : "",
    'dms_id' : "",
    'dms_name' : "",
    'dms_pan' : "",
    'dms_gstin' : "",
    'rlb_id' : "",
    'rlb_name' : "",
    'rlb_pan' : "",
    'rlb_gstin' : "",
    'status' : "",
    'cid' : "",
    'segid' : "",
    'dt_create' : '2020-03-28 23:11:06', #2020-03-28
    'dt_update' : '2020-03-28 23:11:06', #2020-03-28
    'uid_create' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    'uid_update' : "224f02c7-9c81-4b2a-ba8b-54173f061703",
    }

    return data



@pytest.fixture(scope="package")
def url(baseurl):
    urls = { 
        'addLedgermap': baseurl + "/master/ledgermap/add", 
        'updateLedgermap': baseurl + "/master/ledgermap/update/", 
        'getLedgermap': baseurl + "/master/ledgermap/get/", 
        'listLedgermap': baseurl + "/master/ledgermap/list", 
        }
    return urls
