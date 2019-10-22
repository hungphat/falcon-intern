import falcon

class FalconLearn:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

api = falcon.API()
api.add_route('/health', FalconLearn())
