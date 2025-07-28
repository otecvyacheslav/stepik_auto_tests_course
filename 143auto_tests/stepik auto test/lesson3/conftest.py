import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nоткрытие браузера для теста..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nзакрытие браузера..")
    browser.quit()
