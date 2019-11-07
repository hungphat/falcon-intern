from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,class_mapper
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
from falcon_autocrud.resource import CollectionResource, SingleResource
from falcon_autocrud.middleware import Middleware
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
    update_at     = Column(DateTime)

    def __init__(self,  id,  name,   dob,   update_at):
        self.id         = id
        self.name       = name
        self.dob        = dob
        self.update_at  = update_at


#------ CRUD with falcon-autocrud -------
class CustomersCollectionResource(CollectionResource):
    model = Customers
    methods = ['GET', 'POST']

class CustomersResource(SingleResource):
    model = Customers


#----- API Routing -----

api = falcon.API(middleware=[Middleware()],)
api.req_options.auto_parse_form_urlencoded= True
api.add_route('/customers/', CustomersCollectionResource(data_base.engine))
api.add_route('/customers/{id}', CustomersResource(data_base.engine))



