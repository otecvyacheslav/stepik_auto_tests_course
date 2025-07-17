import select

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import math
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"

def calc(x):
    return a1+b1
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a1_stroka = browser.find_element(By.CSS_SELECTOR, "span#num1")
    a1 = int(a1_stroka.text)

    b1_stroka = browser.find_element(By.CSS_SELECTOR, "span#num2")
    b1 = int(b1_stroka.text)
    sum1 = calc(a1+b1)
    #
    print(sum1)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum1))

    go1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    go1.click()

finally:
    time.sleep(5)
    browser.quit()

