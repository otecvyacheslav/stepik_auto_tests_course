from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

def math1(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск  кнопки
    btn1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # клик по кнопке, чтобы вызвать модальное окно
    btn1.click()

    # работа с модальным окном ->
    vspl_confirm = browser.switch_to.alert
    vspl_confirm.accept()

    # ищем Х а странице
    find_x = browser.find_element(By.ID, "input_value")
    # вытягиваем из найденного текст без скобок обязательно
    x = find_x.text
    # задаем У == функция от найденной переменной текста Х
    y = math1(x)

    # находим куда вставить ответ на решение
    input_math_x = browser.find_element(By.ID, "answer")
    # вставляем ответ
    input_math_x.send_keys(y)

    # кнопка сабмит
    enter1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    enter1.click()

finally:
    time.sleep(5)
    browser.quit
