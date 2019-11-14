from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import os; from dotenv import load_dotenv  # Load .env automatically

class connection:
    load_dotenv()
    conect_data = 'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'.format(
        user= os.environ.get('user'),
        pwd=os.environ.get('pwd'),
        host=os.environ.get('host'),
        port=os.environ.get('port'),
        db=os.environ.get('db')
    )

    engine = create_engine(conect_data)
    Session = sessionmaker(bind=engine)
    session = Session()