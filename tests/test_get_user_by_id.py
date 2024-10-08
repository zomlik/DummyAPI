import allure

from api.users_endpoints import Users
from asserts.error_messages import UsersErrors


@allure.suite("Получение пользователя по ID")
class TestGetUserById:
    @allure.title("Получить пользователя по валидному id")
    def test_get_user_by_id(self, id="66f4e0eda75cbd5bcff71591"):
        r = Users()
        r.get_user_by_id(id)
        assert r.status_code_is(200)
        assert r.check_id_is(id)
        assert r.json_schema_get_user_by_id()

    @allure.title("Получить пользователя по не валидному id")
    def test_get_user_by_invalid_id(self):
        r = Users()
        r.get_user_by_id("123abs")
        assert r.status_code_is(400)
        assert r.check_error_message_is(UsersErrors.ID)
