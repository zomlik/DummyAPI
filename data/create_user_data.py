from models.create_user_model import CreateUserModel
from utils.data_generator import DataGenerator


def create_user_json(
    name: str = None,
    email: str = None,
    age: int = None,
    phone: str = None,
    address: str = None,
    role: str = None,
    refcode: str = None,
):
    return CreateUserModel(
        name=DataGenerator.name() if name is None else name,
        email=DataGenerator.email() if email is None else email,
        age=DataGenerator.age() if age is None else age,
        phoneNumber=DataGenerator.phone_number() if phone is None else phone,
        address=DataGenerator.address() if address is None else address,
        role=DataGenerator.role() if role is None else role,
        referralCode=DataGenerator.referral_code() if refcode is None else refcode,
    )
