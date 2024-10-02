import allure
import pytest

from api.users_endpoints import Users
from data.create_user_data import create_user_json
from asserts.error_messages import UsersErrors


@allure.suite("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание пользователя по умолчанию")
    def test_create_user(self):
        r = Users()
        r.create_user(create_user_json())
        assert r.status_code_is(200)
        assert r.json_schema_create_user()

    @allure.title("Создание пользователя с именем '{name}'")
    @pytest.mark.parametrize("name", ["", "    ", "aa"])
    def test_create_user_name_2s(self, name):
        r = Users()
        r.create_user(create_user_json(name=name))
        assert r.status_code_is(400)
        assert r.check_error_message_is(UsersErrors.NAME)

    @allure.title("Создание пользователя с именем из 3 символов")
    def test_create_user_name_3s(self, name: str = "aaa"):
        r = Users()
        r.create_user(create_user_json(name=name))
        assert r.status_code_is(200)
        assert r.check_name_is(name)
        assert r.json_schema_create_user()

    @allure.step("Создание пользователя с email {email}")
    @pytest.mark.parametrize("email", ["123", "@com.ru", "email@man"])
    def test_create_user_invalid_email(self, email):
        r = Users()
        r.create_user(create_user_json(email=email))
        assert r.status_code_is(400)
        assert r.check_error_message_is(UsersErrors.EMAIL)

    @allure.title("Создание пользователя с возрастом {age} лет")
    @pytest.mark.parametrize("age", [18, 20, 119, 120])
    def test_create_user_age_18(self, age):
        r = Users()
        r.create_user(create_user_json(age=age))
        assert r.status_code_is(200)
        assert r.check_age_is(age)
        assert r.json_schema_create_user()

    @allure.title("Создание пользователя с возрастом {age} лет")
    @pytest.mark.parametrize("age", [-1, 0, 17, 121])
    def test_create_user_age_17(self, age):
        r = Users()
        r.create_user(create_user_json(age=age))
        assert r.status_code_is(400)
        assert r.check_error_message_is(UsersErrors.AGE)

    @allure.title("Создание пользователя с не верным телефоном")
    @pytest.mark.parametrize("phone", ["1234567", "+123456", "+12364455655632"])
    def test_create_user_invalid_phone_number(self, phone):
        r = Users()
        r.create_user(create_user_json(phone=phone))
        assert r.status_code_is(400)
        assert r.check_error_message_is(UsersErrors.PHONE_NUMBER)

    @allure.title("Создание пользователя с ролью moderator")
    def test_create_user_role_moderator(self):
        r = Users()
        r.create_user(create_user_json(role="moderator"))
        assert r.status_code_is(200)
        assert r.check_role_is("moderator")
        assert r.json_schema_create_user()

    @allure.title("Создание пользователя без реферального кода")
    def test_create_user_without_refcode(self):
        r = Users()
        r.create_user(create_user_json(refcode=""))
        assert r.status_code_is(200)
        assert r.check_refcode(None)
        assert r.json_schema_create_user()

    @allure.title("Создание пользователя c не верным реферальным кодом")
    def test_create_user_invalid_refcode(self):
        r = Users()
        r.create_user(create_user_json(refcode="ABS"))
        assert r.status_code_is(400)
