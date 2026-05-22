from pydantic import BaseModel

class SigninSchema(BaseModel):
    username: str
    password: str

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str

class UsersSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status:int