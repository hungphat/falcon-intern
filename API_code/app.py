import falcon

class TestResource:  #TODO dat ten tuong` minh thay vi Test
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = ('200')  #TODO ko can

api = falcon.API()
test_resource = TestResource()  #TODO ko can bien test_resource, truyen tr.tiep TestResource() cho add_route()
api.add_route('/health',test_resource)  #TODO sau phay fai co 1 kh.trang
