from fastapi import FastAPI,Depends
import fastapi
import models 
import database 
import schemas
from sqlalchemy.orm import Session
import services


app = FastAPI()

models.database.Base.metadata.create_all(bind=database.engine)

@app.post("/api/create-student")
async def create_student(student:schemas.CreateStudent,db:Session = Depends(services.get_db)):
    new_student = models.Students(name=student.name,department=student.department,email=student.email,mobile=student.mobile,address=student.address)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/api/get-students")
async def get_students(db:Session = Depends(services.get_db)):
    students = db.query(models.Students).all()
    if not students:
        raise fastapi.HTTPException(status_code=404,detail="Database empty")
    return students 