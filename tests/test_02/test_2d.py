from falcon import testing
import json
from api_code.Challenge_2.app2d import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api


    def test_tc00(self):
        r = self.simulate_post(f'/upload/')
        assert r.status_code == 200
