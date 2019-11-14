from connection import *
from customers import *
import json
import falcon

data_sess = connection.session
dataquery = data_sess .query(Customers)
data = dataquery.all()

class CustomersResource:

#------Read------
    def on_get(self, req, resp, id=None):
        if id is None:
            list_data = []
            for customer in data:
                list_data.append(Customers.to_dict(customer))
            resp.body = json.dumps(list_data)
            resp.status = falcon.HTTP_200
        else:
            user = dataquery.get(int(id))
            deltail = Customers.to_dict(user)
            resp.body = json.dumps(deltail)
            resp.status = falcon.HTTP_200


#------Create------
    def on_post(self, req, resp):
        body = req.media
        name = body.get('name')
        dob  = body.get('dob')
        if name is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Data param name is required')
        elif dob is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Data dob is required')
        else:
            id_list = []
            for i in data:
                id_list.append(i.id)
            auto_increaseid = (max(id_list)) + 1
            mess = {
                'id': auto_increaseid
            }
            adduser = Customers(id=auto_increaseid,name = name, dob = dob, updated_at= datetime.now())
            data_sess.add(adduser)
            data_sess.commit()
            resp.body = json.dumps(mess)


#------Update------
    def on_put(self, req, resp, id=None):
        body = req.media
        x = dataquery.get(int(id))
        if body.get('name') is None:
            x.dob = body['dob']
            data_sess.commit()
        elif body.get('dob') is None:
            x.name = body['name']
            data_sess.commit()
        else:
            x.name = body['name']
            x.dob =  body['dob']
            data_sess.commit()
        x.updated_at = datetime.now()
        output = {
                "id": x.id,
                "name": x.name,
                "dob": f'{x.dob}',
                "updated_at": f'{x.updated_at}'
        }
        data_sess.commit()
        resp.body = json.dumps(output)
#------Delete User------
    def on_delete(self, req, resp, id=None):
        x = dataquery.get(int(id))
        data_sess.delete(x)
        data_sess.commit()
        output = {
            "id" : id
        }
        data_sess.commit()
        resp.body = json.dumps(output)
