from connection import *
from crud import *
from customers import *

api = falcon.API()
api.add_route('/customers/', CustomersResource())
api.add_route('/customers/{id}', CustomersResource())