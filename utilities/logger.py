import datetime
import os
from requests import Response


class Logger:
    file_name = f'logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-S')}.log'

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as file_log:
            file_log.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n_____\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {datetime.datetime.now()}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        cookies = dict(result.cookies)
        headers = dict(result.headers)

        data_to_add = f'Status code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers}\n'
        data_to_add += f'Response cookies: {cookies}\n'
        data_to_add += f'\n_____\n'

        cls.write_log_to_file(data_to_add)
