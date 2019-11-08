import falcon
import datetime
import json
from string import punctuation

class HealthResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

class HelloResource:
    def on_get(self, req, resp, name=None):
        try:
            int(name)
            resp.status = falcon.HTTP_404
            resp.body = ('Interger not accept')
        except ValueError:
            count =0
            for i in name:
                count += punctuation.count(i)
            if count >0:
                resp.status = falcon.HTTP_404
                resp.body = ('Interger not accept')
            else:
                resp.body = (f'Hello {name}')

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
    def on_get(self, req, resp, name=None):
        if name is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Param :name is required')
        else:
            try:
                int(name)
                resp.status = falcon.HTTP_404
                raise falcon.HTTPBadRequest('Param :name must be a valid string')
            except ValueError:
                count = 0
                for i in name:
                    count += punctuation.count(i)
                if count > 0:
                    resp.status = falcon.HTTP_404
                    raise falcon.HTTPBadRequest('Param :name must be a valid string')
                else:
                    resp.body = (f'Hola {name}')



api = falcon.API()
api.req_options.auto_parse_form_urlencoded=True
api.add_route('/health', HealthResource())
api.add_route('/hi', HiResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hello/', HelloResource())
api.add_route('/hola/{name}', HolaResource())
api.add_route('/hola/', HolaResource())

# for i in data:
#     if i.name == body['name']:
#         out_put = {
#             "id": i.id
#         }
#         resp.body = json.dumps(out_put)