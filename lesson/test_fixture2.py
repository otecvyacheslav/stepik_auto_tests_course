import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture #если закомментить это, то не назначяются фикстуры....
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1:
    # сейчас пойдет вызов фикстуры
    def test_quest_see_login_link(self, browser):
        # селф это что-то типа объекта, не вдаюсь в подробности пока, а вот browser это ранее объявленнаяы функция, которую мы тут вызываем
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_quest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
