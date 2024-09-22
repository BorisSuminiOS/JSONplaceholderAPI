import json
from requests import Response


class Checking:
    """Проверки ответов от сервера"""

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
    def check_list_names_users(response: Response):
        result = response.json()
        names = [i.get('name') for i in result]
        assert len(names) > 0, "Список имен пользователей пустой"
        print(f'Проверка списка имен пользователей: [{len(names)}] имен. Список не пустой')

    @staticmethod
    def check_list_users(response: Response):
        result = response.json()
        users = [i for i in result]
        assert len(users) > 0, "Список пользователей пустой"
        print(f'Проверка списка пользователей: [{len(users)}] пользователей. Список не пустой')

    @staticmethod
    def check_list_user_fields(response: Response, required_fields):
        result = response.json()
        users = [[*i.keys()] for i in result]
        for k,v in enumerate(users):
            assert required_fields == v, "Указанные поля не найдены"
            print(f"Проверка полей: У пользователя №{k + 1} все поля присутствуют\n {required_fields}")

    @staticmethod
    def check_field_email(response: Response):
        result = response.json()
        email = [i.get('email') for i in result]
        for k,v in enumerate(email):
            assert "@" in v, f"Указанный знак у пользователя {v} отсутствует"
            print(f"Проверка поле Email: У пользователя №{k + 1} в email присутствует символ '@'")



