from utilities.http_methods import Http_methods

base_url = 'https://jsonplaceholder.typicode.com'


class JsonPlaceholderApi:
    '''API методы, create, read, update, delete users (CRUD)'''


    @staticmethod
    def get_users():
        '''Показать список пользователей'''

        resource_get = '/users'
        url = f'{base_url}{resource_get}'
        result_get = Http_methods.get(url)
        print(f'Ответ от сервера: {result_get.text}')
        print(f'Файтический статус код: {result_get.status_code}')
        return result_get