from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group.first_class input")
    input1.send_keys('Olesya')
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group.second_class input")
    input2.send_keys('Voropaeva')
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group.third_class input")
    input3.send_keys('моя почта - секрет фирмы))')

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    time.sleep(10)
    browser.quit()

