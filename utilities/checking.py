import json
from requests import Response


class Checking:
    '''Проверки ответов от сервера'''

    @staticmethod
    def check_status_code(response: Response, status_code):
        status_code_response = response.status_code
        assert status_code_response == status_code
        print(f'Проверка на статус код: Успешно [{status_code_response}]')

    @staticmethod
    def check_all_required_fields(response: Response, required_fields):
        required_fields_response = json.loads(response.text)
        assert required_fields_response == required_fields
        print(f"Обязательные поля: Все указанные поля в ответе от сервера присутствуют")

    @staticmethod
    def check_json_value(response: Response, key, value):
        response_value = json.loads(response.text).get(key)
        assert response_value == value
        print(f"Обязательное поле {key} со значением {value} присутствует в ответе от сервера")


    @staticmethod
    def check_list_names_users(response: Response, ):
        result = response.json()
        names = [i.get('name') for i in result]
        assert len(names) > 0
        print(f'Проверка списка имен пользователей: [{len(names)}] имен. Список не пустой')

    @staticmethod
    def check_list_users(response: Response):
        result = response.json()
        users = [i for i in result]
        assert len(users) > 0
        print(f'Проверка списка пользователей: [{len(users)}] пользователей. Список не пустой')

    @staticmethod
    def check_list_user_fields(response: Response, required_fields):
        result = response.json()
        users = [[*i.keys()] for i in result]
        for k,v in enumerate(users):
            assert required_fields == v
            print(f"Проверка полей: У пользователя №{k + 1} все поля присутствуют \n {required_fields}")

    @staticmethod
    def check_list_names_users(response: Response, ):
        result = response.json()
        names = [i.get('name') for i in result]
        assert len(names) > 0
        print(f'Проверка списка имен пользователей: [{len(names)}] имен. Список не пустой')

