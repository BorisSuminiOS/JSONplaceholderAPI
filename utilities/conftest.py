import pytest


@pytest.fixture(scope='function')
def test_delimitation():
    print('Начало тестирования модуля test_json_placeholer')
    yield
    print('Завершение тестирования модуля test_json_placeholer')
