from pydantic import BaseModel # for authentication of data input

class SignupSchema(BaseModel):
     fullname:str
     phone:str
     email:str
     password:str
     
class SigninSchema(BaseModel):
    username:str
    password:str
    
class UserSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status:int
    
class TaskSchema(BaseModel):
    title:str
    description:str
    createdby:int
    assignedto:int
    priority:int
    deadline:str
    status:int