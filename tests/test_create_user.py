import allure
from api.users_endpoints import Users
from data.create_user_data import create_user_json

@allure.suite("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание пользователя по умолчанию")
    def test_create_user(self):
        r = Users()
        r.create_user(create_user_json())
        assert r.status_code_is(200)
        assert r.check_status_is_created()
        assert r.json_schema_create_user()

    @allure.title("Создание пользователя с именем из 2 символов")
    def test_create_user_name_2s(self):
        r = Users()
        r.create_user(create_user_json(name="aa"))
        assert r.status_code_is(400)
        assert r.check_error_message_is("Invalid name: it must be a string with at least 3 characters")

    @allure.title("Создание пользователя с именем из 3 символов")
    def test_create_user_name_3s(self, name: str = "aa"):
        r = Users()
        r.create_user(create_user_json(name=name))
        assert r.status_code_is(200)
        assert r.check_status_is_created()
        assert r.check_name_is(name)
        assert r.json_schema_create_user()




