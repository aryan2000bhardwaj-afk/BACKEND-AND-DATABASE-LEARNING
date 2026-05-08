from pydantic import BaseModel

class SigninSchema(BaseModel):
    email: str
    password: str

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str