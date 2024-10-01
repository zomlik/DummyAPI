import os
import requests
import allure
from utils.logger import log


class ApiClient:
    _TOKEN = os.environ.get("TOKEN")
    _HEADERS = {"Authorization": f"Bearer {_TOKEN}"}

    def __init__(self):
        self.response = None

    def get(self, url: str, query: dict = None):
        self.response = requests.get(url=url, params=query, headers=self._HEADERS)
        log(response=self.response)

    def post(self, url: str, json_body: dict = None):
        self.response = requests.post(url=url, json=json_body, headers=self._HEADERS)
        log(response=self.response, json=json_body)

    def put(self, url: str, json_body: dict = None):
        self.response = requests.put(url=url, json=json_body, headers=self._HEADERS)
        log(response=self.response, json=json_body)

    def delete(self, url: str):
        self.response = requests.delete(url=url, headers=self._HEADERS)

    @allure.step("Статус код {code}")
    def status_code_is(self, code: int):
        return self.response.status_code == code

    def get_json(self):
        json = self.response.json()
        return json

    # JSON
    @allure.step("ID присутствует в ответе")
    def check_id_is(self, id: str):
        return self.get_json()["id"] == id

    @allure.step("Name присутствует в ответе")
    def check_name_is(self, name: str):
        return self.get_json()["name"] == name

    @allure.step("Поле status created")
    def check_status_is_created(self, status: str = "created"):
        return self.get_json()["status"] == status

    @allure.step("Ошибка {msg}")
    def check_error_message_is(self, msg: str):
        return self.get_json()["error"] == msg
