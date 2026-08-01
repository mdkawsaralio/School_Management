from fastapi import APIRouter, Depends,HTTPException, Path,status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Annotated
from database import Session_local
from model import Student

router=APIRouter()

class create_data(BaseModel):
    name:str =Field(max_length=50)
    roll: int =Field(gt=0)
    Class_name: str =Field(max_length=20)
    father_name: str =Field(max_length=50)
    mother_name:str =Field(max_length=50)
    address: str =Field(max_length=60)


def db_connect():
    db=Session_local()
    try:
        yield db
    finally:
        db.close()

data_dependency=Annotated[Session,Depends(db_connect)]

@router.get("/",status_code=status.HTTP_200_OK)
async def read_all(db:data_dependency):
    return db.query(Student).all()


@router.post("/create_student",status_code=status.HTTP_201_CREATED)
async def create_student(db:data_dependency,create_student:create_data):
    student_model=Student(**create_student.model_dump())
    db.add(student_model)
    db.commit()
    return db.query(Student).all()

@router.get("/search/{id}",status_code=status.HTTP_200_OK)
async def search_by_id(db:data_dependency,id:int=Path(gt=0)):
    student_model=db.query(Student).filter(Student.id==id).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="File Not Found")
    return student_model

@router.put("/update/{id}")
async def update_by_id(db:data_dependency,update_data:create_data,id:int=Path(gt=0)):
    student_model=db.query(Student).filter(Student.id==id).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    student_model.name= update_data.name
    student_model.roll=update_data.roll
    student_model.Class_name=update_data.class_name
    student_model.father_name=update_data.father_name
    student_model.mother_name=update_data.mother_name
    student_model.address=update_data.address
    db.commit()
    return db.query(Student).all()

@router.delete("/delete/{id}")
async def delete_by_id(db:data_dependency,id:int =Path(gt=0)):
    student_model=db.query(Student).filter(Student.id==id).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found")
    db.delete(student_model)
    db.commit()
    return db.query(Student).all()

@router.get("/search_roll/{roll}",status_code=status.HTTP_200_OK)
async def search_by_roll(db:data_dependency,roll:int=Path(gt=0)):
    student_model=db.query(Student).filter(Student.roll==roll).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="File Not Found")
    return student_model

@router.delete("/delete_roll/{roll}")
async def delete_by_roll(db:data_dependency,roll:int =Path(gt=0)):
    student_model=db.query(Student).filter(Student.roll==roll).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found")
    db.delete(student_model)
    db.commit()
    return db.query(Student).all()


@router.put("/update_roll",)
async def update_by_roll(db:data_dependency,update_data:create_data):
    student_model=db.query(Student).filter(Student.roll==update_data.roll).first()
    if student_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    student_model.name= update_data.name
    student_model.roll=update_data.roll
    student_model.Class_name=update_data.class_name
    student_model.father_name=update_data.father_name
    student_model.mother_name=update_data.mother_name
    student_model.address=update_data.address
    db.commit()
    return db.query(Student).all()