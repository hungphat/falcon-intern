import falcon
import json
from string import punctuation

class HealthResource:
    def on_get(self, req, res):
        content = {}
        res.body = json.dumps(content)


class HelloResource:
    def on_get(self, req, resp, name=None, lastname= None):
        if name is None and lastname is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Params are required')
        elif lastname is None:
            raise falcon.HTTPBadRequest('All params are required')
        else:
            try:
                int(name)
                resp.status = falcon.HTTP_404
                raise falcon.HTTPBadRequest('All params must be valid')
            except ValueError:
                count = 0
                for i in name:
                    count += punctuation.count(i)
                if count > 0:
                    resp.status = falcon.HTTP_404
                    raise falcon.HTTPBadRequest('All params must be valid')
                else:
                    content = {
                        'output' : 'Hello {name} {lastname}'.format(name=name, lastname=lastname)
                    }
                resp.body = json.dumps(content)


api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}/{lastname}', HelloResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hello/', HelloResource())
