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
    def on_post(self, req, resp):
        # body = json.loads(req.stream.read())
        body = req.media  # 2 code tuong duong
        for k,v in body.items():
            if v == '':
                resp.status = falcon.HTTP_404
                raise falcon.HTTPBadRequest('all values cannot be empty')
        for k,v in body.items():
            try:
                int(v)
                resp.status = falcon.HTTP_404
                raise falcon.HTTPBadRequest('all values ​​must be valid')
            except ValueError:
                count = 0
                for i in v:
                    count += punctuation.count(i)
                if count > 0:
                    resp.status = falcon.HTTP_404
                    raise falcon.HTTPBadRequest('all values ​​must be valid')
        name =body['fname']
        lastname = body['lname']
        content = {
            'message': 'Hello{name} {lastname}'.format(name=name, lastname=lastname)
        }
        resp.body = json.dumps(content)


api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/form/', FormResource())
api.add_route('/hello/', FormBodyResource())
