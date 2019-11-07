from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,class_mapper,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
import json
import falcon

class data_base:
    conect_data = 'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'.format(
        user='admin',
        pwd='admin',
        host='localhost',
        port='5432',
        db='customerdata'
    )

    engine = create_engine(conect_data)
    Session = sessionmaker(bind=engine)
    session = Session()

dt = datetime.now()
Base = declarative_base()
data_sess = data_base.session


class Customers(Base):
    __tablename__ = 'customers'
    id            = Column(Integer,    primary_key=True)
    name          = Column(String)
    dob           = Column(Date)
    updated_at     = Column(DateTime)

    def __init__(self,  id,  name,   dob,   updated_at):
        self.id         = id
        self.name       = name
        self.dob        = dob
        self.updated_at  = updated_at

    def to_dict(self):
        d = {
            "id"         : self.id,
            "name"       : self.name,
            "dob"        : self.dob.__str__(),
            "updated_at"  : self.updated_at.__str__()
        }
        return d

dataquery = data_sess.query(Customers)
data = dataquery.all()
#------CRUD with falcon-------

class CustomersResource:

#------Read------
    def on_get(self, req, resp, id=None):
        if id is None:
            list_data = []
            data = dataquery.all()
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
        if body['name'] is None:
            raise falcon.HTTPBadRequest('Data param name is required')
        elif body['dob'] is None:
            raise falcon.HTTPBadRequest('Data param dob is required')



        #------Update------
    def on_put(self, req, resp, userid=None):
        pass


#------Delete User------
    def on_delete(self, req, resp, userid=None):
        pass
#------API Routing------
api = falcon.API()
api.add_route('/customers/', CustomersResource())
api.add_route('/customers/{id}', CustomersResource())

