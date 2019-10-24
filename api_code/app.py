import falcon
import datetime

time_stamp = datetime.datetime.now()


class HealthResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

class HelloResource:
    def on_get(self, req, resp, name):
        resp.body   = (f'Hello {name}')

class HiResource:
    def on_get(self, req, resp):
        if time_stamp.hour >= 7 and time_stamp.hour <=11:
            resp.body = ('Good Morning')
        elif time_stamp.hour >11 and time_stamp.hour <=15:
            resp.body = ('Good afternoon')
        else:
            resp.body = ('Good evening')



api = falcon.API()
api.add_route('/health', HealthResource())
api.add_route('/hi', HiResource())
api.add_route('/hello/{name}', HelloResource())
