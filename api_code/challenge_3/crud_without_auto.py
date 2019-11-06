from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,class_mapper
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
    birth         = Column(Date)
    address       = Column(String)
    phone         = Column(String)
    update_at     = Column(DateTime)

    def __init__(self,  id,  name,   birth,  address,   phone,    update_at):
        self.id      = id
        self.name    = name
        self.birth   = birth
        self.address = address
        self.phone   = phone
        self.update_at  = update_at
id_list = []
dataquery = data_sess.query(Customers)
for read in dataquery:
    id_list.append(read.id)

class HealthResource:
    def on_get(self, req, res):
        content = {}
        res.body = json.dumps(content)

#------CRUD with falcon-------

class CustomersResource(object):

# ---Read---
    def on_get(self, resp, req, userid=None):
        if int(userid) not in id_list:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('ID not in database')
        else:
            Hello = {
                'Message' : 'Welcome'
            }
            resp.body = json.dumps(Hello)

#------Create------
    def on_post(self, req, resp): #TODO : Anh Nam xem giup em viet dung y anh chua a ?
        body = req.media
        adduser = Customers(id        =  body['id'],
                            name      =  body['name'],
                            birth     =  body['dob'],
                            address   =  body['address'],
                            phone     =  body['phone'],
                            update_at =  datetime.now())
        data_sess.add(adduser)
        data_sess.commit()

#-----Update------
    def on_put(self, req, resp, userid=None):
        pass


#-- Delete User
    def on_delete(self, req, resp, userid=None):
        pass
#-----API Routing-----
api = falcon.API()
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/health', HealthResource())
api.add_route('/customer/', CustomersResource())
api.add_route('/customer/{userid}', CustomersResource())

