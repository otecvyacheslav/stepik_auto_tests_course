import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose your language: ru, en, ec, fr')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_language': user_language})
    print('\nstart browser..')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print('\nclose browser..')
    browser.quit()


