from utilities.checking import Checking
import allure
from utilities.json_placeholder_api import JsonPlaceholderApi



@allure.epic('Тестирование пользователей')
class TestJsonPlaceholder:

    @classmethod
    @allure.description('Тест на отображение пользователей')
    def test_get_users(cls):
        list_custom_fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
        response = JsonPlaceholderApi.get_users()
        Checking.check_status_code(response, 200)
        Checking.check_list_names_users(response)
        Checking.check_list_users(response)
        Checking.check_list_user_fields(response, list_custom_fields)


