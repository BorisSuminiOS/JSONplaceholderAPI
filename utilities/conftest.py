import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def web_diver():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # driver.close()


@pytest.fixture(scope='module')  # function, cls - не только модуль, но и функция или класс
def some():
    print('Enter System')
    yield
    print('Exit System')
