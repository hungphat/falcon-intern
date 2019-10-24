from api_code.app import api
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

    def test_01b(self):
        INPUT_name = 'phat'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code == 200
        assert r.text == f'Hello {INPUT_name}'

    def test_02(self):
        r = self.simulate_get(f'/hi')
        assert r.status_code == 200
        assert r.text == f'Good Afternoon'