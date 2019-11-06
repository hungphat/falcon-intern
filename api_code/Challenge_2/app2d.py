import falcon
import json
from falcon import media
from string import punctuation


class HealthResource:
    def on_get(self, req, res):
        content = {}
        res.body = json.dumps(content)

class UploadFileResource:
    def on_post(self, req, resp):

        pass




#----- API Routing------
api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/upload/', UploadFileResource())
