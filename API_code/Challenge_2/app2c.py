import falcon
import json
from string import punctuation

class HealthResource:
    def on_get(self, req, res):
        content = {}
        res.body = json.dumps(content)



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
