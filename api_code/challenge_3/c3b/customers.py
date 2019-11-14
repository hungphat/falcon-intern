from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
from connection import connection

dt = datetime.now()
Base = declarative_base()

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
