from utilities.checking import Checking
import allure
from utilities.json_placeholder_api import JsonPlaceholderApi
from utilities.conftest import test_delimitation


@allure.epic('Тестирование пользователей')
class TestJsonPlaceholder:

    @allure.description('Тест на отображение пользователей')
    def test_get_users(self,test_delimitation):
        response = JsonPlaceholderApi.get_users()
        Checking.check_status_code(response, 200)
        Checking.check_list_names_users(response)
        Checking.check_list_users(response)
        Checking.check_list_user_fields(response,['id',
                                                  'name',
                                                  'username',
                                                  'email',
                                                  'address',
                                                  'phone',
                                                  'website',
                                                  'company'])
        Checking.check_field_email(response)



