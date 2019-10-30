from api_code.Challenge_2.app import api
from falcon import testing


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_tc00(self):
        r = self.simulate_get('/health')
        assert r.status_code == 200
        assert r.json == {}

    def test_tc01(self):
        INPUT_firstname = 'phat'
        INPUT_lastname = 'nguyen'
        r = self.simulate_get(f'/hello/{INPUT_firstname}/{INPUT_lastname}')
        assert r.status_code == 200
        assert r.json == {'output': 'Hello phat nguyen'}

    def test_tc02(self):
        r = self.simulate_get(f'/form')
        assert r.status_code == 200

        
