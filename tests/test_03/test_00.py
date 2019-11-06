from falcon import testing
import json
from api_code.challenge_3.crud_without_auto import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        r = self.simulate_get(f'/health')

    def test_01(self):
        r = self.simulate_get(f'/customer/1')
        assert r.status_code == 200

    def test_02(self):
        body = {
            'name'    : 'Trung',
            'dob'     : '1993-11-11',
            'id'      : '9',
            'address' : 'Ha Noi',
            'phone'   : '1234445'
        }
        r = self.simulate_post(f'/customer/', body=json.dumps(body))
        assert r.status_code == 200

    def test_03(self):
        body = {
            'name'    : 'Thang',
            'dob'     : '1993-11-11',
            'id'      : '1',
            'address' : 'Ha Noi',
            'phone'   : '1234445'
        }
        r = self.simulate_post(f'/customer/1', body=json.dumps(body))
        assert r.status_code == 200

