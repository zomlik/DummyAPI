from pydantic import BaseModel


class DecodeToken(BaseModel):
    userId: str
    iat: int
    exp: int


class GetUserModel(BaseModel):
    id: str
    name: str
    email: str
    age: int
    phoneNumber: str
    address: str
    role: str
    referralCode: str
    createdAt: str
    createdBy: str
    decodedToken: DecodeToken
