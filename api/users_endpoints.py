import allure
from pydantic import ValidationError

from api.api import ApiClient
from api.routes import Routes
from models.create_user_model import CreateUserModel, ResponseCreateUserModel
from models.get_user_model import GetUserModel


class Users(ApiClient):
    @allure.step("Создание пользователя")
    def create_user(self, data: CreateUserModel):
        return self.post(Routes.CREATE_USER, json_body=data.model_dump())

    @allure.step("Получение пользователя по id")
    def get_user_by_id(self, user_id: str):
        return self.get(url=f"{Routes.GET_USER_BY_ID}/{user_id}")

    @allure.step("Получение всех пользователей")
    def get_list_users(self):
        return self.get(url=Routes.GET_USERS)

    # Schema
    def json_schema_get_user_by_id(self):
        data = self.get_json()
        try:
            GetUserModel(**data)
            return True
        except ValidationError:
            return ValidationError()

    # JSON
    @allure.step("Возраст {age}")
    def check_age_is(self, age):
        return self.get_json()["age"] == age

    @allure.step("Роль {role}")
    def check_role_is(self, role):
        return self.get_json()["role"] == role

    @allure.step("Реферальный код {refcode}")
    def check_refcode(self, refcode):
        return self.get_json()["referralCode"] == refcode

    @allure.step("Схема 'Создание пользователя' валидна")
    def json_schema_create_user(self):
        data = self.get_json()
        try:
            ResponseCreateUserModel(**data)
            return True
        except ValidationError:
            ValidationError()
