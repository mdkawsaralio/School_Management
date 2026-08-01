from fastapi import FastAPI
import model
from database import engine
from routers import student

app=FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(student.router)