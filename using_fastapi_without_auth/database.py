
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_url='postgresql://postgres:kawsar@localhost/student'

engine=create_engine(sql_url)

Session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
