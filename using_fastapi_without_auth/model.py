from database import Base
from sqlalchemy import Column,Integer,String


class Student(Base):
    __tablename__='student'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    roll=Column(Integer,nullable=False)
    Class_name=Column(String,nullable=False)
    father_name=Column(String,nullable=False)
    mother_name=Column(String,nullable=False)
    address=Column(String,nullable=False)

