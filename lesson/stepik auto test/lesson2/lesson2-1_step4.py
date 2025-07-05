from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываю браузер
    browser = webdriver.Chrome()
    # открываю ссылку из переменной линк
    browser.get(link)

    # здесь будет решение примера и его установка в ответ
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input3 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input3.send_keys(y)

    # check box
    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()
    # radio button
    radio1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio1.click()
    # submit1
    go1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    go1.click()

finally:
    time.sleep(10)
    browser.quit()
