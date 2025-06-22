import select

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import math
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects2.html"

def calc(x): # создаем функцию calc
    return a1+b1 # указываем что будет происходить при ее использовании
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a1_stroka = browser.find_element(By.CSS_SELECTOR, "span#num1") # ищем строку
    a1 = int(a1_stroka.text) # задаем найденное как целое число

    b1_stroka = browser.find_element(By.CSS_SELECTOR, "span#num2") # ищем строку
    b1 = int(b1_stroka.text) # задаем нацденное как целое число
    sum1 = calc(a1+b1) # указываем назначение переменной с использованием функции calc

    print(sum1) # вывожу в консоль значение, чтобы быть уверенным в подсчете

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown")) # находим необходимую строку
    select.select_by_value(str(sum1)) # выбираем в ней значение равное переменной sum

    go1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")# находим необходимую строку
    go1.click()# кликаем

finally:
    time.sleep(5) # заминка 5 секунд
    browser.quit() # закрытие браузера

