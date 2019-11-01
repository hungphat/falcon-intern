from falcon import testing
import json
from api_code.Challenge_2.app2c import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api


    def test_tc00(self):
        body = {
            'fname': '',
            'lname': ''
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values cannot be empty' in e

    def test_tc0a(self):
        body = {
            'fname': 'abc',
            'lname': ''
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values cannot be empty' in e


    def test_tc01(self):
        body = {
            'fname': '123',
            'lname': '@#$'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values ​​must be valid' in e

    def test_tc01a(self):
        body = {
            'fname': '',
            'lname': '@#$'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values ​​must be valid' in e


    def test_tc02(self):
        body = {
            '': 'abc',
            '': 'abc'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all key cannot be empty' in e

    def test_tc02a(self):
        body = {
            'fname': 'abc',
            '': 'abc'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all key cannot be empty' in e


    def test_tc03(self):
        body = {
            'not_fname': 'abc',
            'not_lname': 'abc'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'key must be fname and lname' in e

    def test_tc03a(self):
        body = {
            'fname': 'abc',
            'not_lname': 'abc'
        }
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'key must be fname and lname' in e


    def test_tc04(self):
        first_name = 'some first name'
        last_name = 'some last name'
        body = {
            'fname': f'{first_name}',
            'lname': f'{last_name}'
        }
        d = {
            'message': f'Hello{first_name} {last_name}'
            }
        expected_out = json.dumps(d)
        r = self.simulate_post(f'/hello/', body=json.dumps(body))
        assert r.status_code == 200
        assert r.text == expected_out
