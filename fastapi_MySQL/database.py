from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://{root}:{password}@{host}:{port}/{database}'.format(
    root='root',
    password='1157139',
    host='localhost',
    port=3306,
    database='ssafy'
)

class engineconn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session


    def connection(self):
        conn = self.engine.connect()
        return conn
    
