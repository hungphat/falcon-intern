from api_code.Challenge_1.app import api
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

