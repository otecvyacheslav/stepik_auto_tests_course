from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
# from selenium.webdriver.support.ui import Select


link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    zn_x = browser.find_element(By.CSS_SELECTOR, "#input_value") # поиск поля, где есть значение х

    x = zn_x.text # переменная == текст из поля zn_x
    y = calc(x)

    input12 = browser.find_element(By.CSS_SELECTOR, "#answer") # поиск поля ввода
    input12.send_keys(y) # передача в поле переменой input значения из переменной у

    # прокрутка вниз до поля submit, а также клик
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # вводим значение, которое получили в функции

    # выбираем конкретный чек бокс
    check = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    check.click()

    # ставим конкретный радио баттон
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    # кликаем по переменной button
    button.click()

finally:
    time.sleep(5) # заминка 5 секунд
    browser.quit() # закрытие браузера

