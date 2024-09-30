from pydantic import BaseModel
from typing import Optional


class CreateUserModel(BaseModel):
    name: str
    email: str
    age: int
    phoneNumber: str
    address: str
    role: str
    referralCode: str = None

class ResponseCreateUserModel(BaseModel):
    name: str
    email: str
    age: int
    phoneNumber: str
    address: str
    role: str
    referralCode: str = None
    status: str