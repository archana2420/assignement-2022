import pydantic

class CreateStudent(pydantic.BaseModel):
    name:str
    department:str
    email:str
    mobile:int
    address:str 

class Student(CreateStudent):
    id:int 

    class Config:
        orm_mode = True 
