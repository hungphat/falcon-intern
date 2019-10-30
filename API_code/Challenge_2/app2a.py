import falcon
import json
from string import punctuation

class HealthResource:
    def on_get(self, req, res):
        content = {}
        res.body = json.dumps(content)


class HelloResource:
    def on_get(self, req, resp, name=None):
        if name is None:
            resp.status = falcon.HTTP_404
        else:
            try:
                int(name)
                resp.status = falcon.HTTP_404
            except ValueError:
                count = 0
                for i in name:
                    count += punctuation.count(i)
                if count > 0:
                    resp.status = falcon.HTTP_404
                else:
                    content = {
                        'output' : 'Hello {name}'.format(name=name)
                    }
                    resp.body = json.dumps(content)




class HolaResource:
    def on_get(self, req, resp, name=None):
        if name is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('name is required')
        else:
            try:
                int(name)
                resp.status = falcon.HTTP_404
                raise falcon.HTTPBadRequest('name must be a valid string')
            except ValueError:
                count = 0
                for i in name:
                    count += punctuation.count(i)
                if count > 0:
                    resp.status = falcon.HTTP_404
                    raise falcon.HTTPBadRequest('name must be a valid string')
                else:
                        content = {
                            'output': 'Hola {name}'.format(name=name)
                        }
            resp.body = json.dumps(content)

class FormResource(object):
    def on_post(self, req, resp):
        firstname = req.get_param("firstname")
        lastname  = req.get_param("lastname")
        content = {
            'firstname': '{firstname}'.format(firstname=firstname),
            'lastname' : '{lastname}' .format(lastname=lastname)
        }

        resp.body = json.dumps(content)

class FormBodyResource(object):
    def on_post(self, req, resp):
        firstname = req.get_param("firstname")
        lastname  = req.get_param("lastname")
        content = {
            'firstname': '{firstname}'.format(firstname=firstname),
            'lastname' : '{lastname}' .format(lastname=lastname)
        }

        resp.body = json.dumps(content)



api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}/{lastname}', HelloResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hello/', HelloResource())
api.add_route('/hola/{name}', HolaResource())
api.add_route('/hola/', HolaResource())
api.add_route('/form', FormResource())
api.add_route('/formbody', FormBodyResource())
