from utilities.checking import Checking
import allure
from utilities.json_placeholder_api import JsonPlaceholderApi


@allure.epic('Тестирование пользователей')
class TestJsonPlaceholder:

    @classmethod
    @allure.description('Тест на отображение пользователей')
    def test_get_users(cls):
        response = JsonPlaceholderApi.get_users()
        Checking.check_status_code(response, 200)
        Checking.get_list_names_users(response)
        Checking.get_list_users(response)