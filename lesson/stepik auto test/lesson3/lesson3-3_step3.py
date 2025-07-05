import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.first_class input"
    )
    input1.send_keys("Иван")
    input3 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.third_class input"
    )
    input3.send_keys("моя почта - секрет фирмы))")
    input2 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.second_class input"
    )
    input2.send_keys("Васильевич")
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert (
        "Congratulations! You have successfully registered!" == welcome_text,
        "Тест не пройден, проверь тест 1",
    )


def test_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.first_class input"
    )
    input1.send_keys("Иван")
    input3 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.third_class input"
    )
    input3.send_keys("моя почта - секрет фирмы))")
    input2 = browser.find_element(
        By.CSS_SELECTOR, ".first_block>.form-group.second_class input"
    )
    input2.send_keys("Васильевич")
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert (
        "Congratulations! You have successfully registered!" == welcome_text,
        "Тест не пройден, проверь тест 2",
    )


if __name__ == "__main__":
    pytest.main()
