import falcon
import datetime
from falcon import HTTPError

class HealthResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

class HelloResource:
    def on_get(self, req, resp, name):
        resp.body   = (f'Hello {name}')

class HiResource:
    def on_get(self, req, resp):
        time_stamp = datetime.datetime.now()
        if time_stamp.hour >= 0 and time_stamp.hour <12:
            resp.body = ('Good Morning')
        elif time_stamp.hour >= 12 and time_stamp.hour <18:
            resp.body = ('Good afternoon')
        else:
            resp.body = ('Good evening')

class HolaResource:
    def on_get(self, req, resp, name):
        if name == None:
            resp.body = ('Must have name')
        else:
            resp.body = (f'Hello {name}')

class HolaResourceException(HolaResource):
    def handle(ex, req, resp, params):
        raise falcon.HTTPError(falcon.HTTP_404)

def error_handler(ex, req, resp, params):
    resp.body = ('Http Error')


api = falcon.API()
api.add_route('/health', HealthResource())
api.add_route('/hi', HiResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hola/{name}', HolaResource())
api.add_error_handler(Exception, error_handler)