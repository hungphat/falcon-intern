import falcon
import json
from falcon import media
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
    def on_post(self, req, resp, **kwargs):
        # body = json.loads(req.stream.read())
        body = req.media  # 2 code tuong duong
        if 'lname' not in body:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('all key cannot be empty')
        else:
            firstname = body['fname']
            lastname = body['lname']
            content = {
                'message': f'Hello{firstname} {lastname}'
            }

        resp.body = json.dumps(content)


api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/form/', FormResource())
api.add_route('/hello/', FormBodyResource())
