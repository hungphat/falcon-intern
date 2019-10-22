import falcon

class TestResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

        res.body = ('200')

api = falcon.API()
test_resource = TestResource()
api.add_route('/health',test_resource)
