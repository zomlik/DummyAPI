import allure
from pydantic import ValidationError

from api.api import ApiClient
from api.routes import Routes
from models.create_user_model import CreateUserModel, ResponseCreateUserModel
from models.get_user_model import GetUserByIdModel


class Users(ApiClient):
    @allure.step("Создание пользователя")
    def create_user(self, data: CreateUserModel):
        return self.post(Routes.CREATE_USER, json_body=data.model_dump())

    @allure.step("Получение пользователя по id")
    def get_user_by_id(self, user_id: str):
        return self.get(url=f"{Routes.GET_USER}/{user_id}")

    @allure.step("Получение всех пользователей")
    def get_list_users(self):
        return self.get(url=Routes.GET_USERS)

    # Schema
    def json_schema_get_user_by_id(self):
        data = self.get_json()
        try:
            GetUserByIdModel(**data)
            return True
        except ValidationError:
            return ValidationError()

    def json_schema_create_user(self):
        data = self.get_json()
        try:
            ResponseCreateUserModel(**data)
            return True
        except ValidationError:
            ValidationError()
