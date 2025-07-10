from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

# from login_password import login
# from login_password import password


link = "https://erp.solforb.ru/Test/ASUReact/login"


@pytest.fixture(scope="class")
def browser():
    print("\nзапуск браузера")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nзакрытие браузера")
    browser.quit()


class Test_input_login_password:
    def test_first_page(self, browser):
        browser.get(link)
        login = browser.find_element(By.CSS_SELECTOR, "[name=Login]")
        print("\nввод логина")
        login.send_keys("support")
        password = browser.find_element(By.CSS_SELECTOR, "[name=Password]")
        print("\nввод пароля")
        password.send_keys("Solforb.2015")
        button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
        button.click()
        print("\nмы зашли на страницу Рабочий кабинет")


class Test_Page_рабочий_стол(Test_input_login_password):
    def test_page_неснижаемые_остатки(self, browser):
        
class TestPageZMK(Test_input_login_password):
    def test_zmk_page(self, browser):
        print("\nклик на меню")
        menu1 = browser.find_element(
            By.CSS_SELECTOR, ".nav-collapse > ul > li.dropdown > a"
        )
        menu1.click()
        print("\nклик на змк")
        zmk1 = browser.find_element(
            By.CSS_SELECTOR, "[href='https://erp.solforb.ru/TEST/ASUCommon/psk/Zmk']"
        )
        zmk1.click()
        time.sleep(3)
