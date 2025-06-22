import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/redirect_accept.html"


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    troll = browser.find_element(By.CLASS_NAME, "trollface")
    troll.click()

    wind2 = browser.window_handles[1]
    browser.switch_to.window(wind2)
    # поиск элемента, где спрятно значение Х
    x_text = browser.find_element(By.ID, "input_value")
    # берем значение из найденной строки
    x = x_text.text
    # добавляем функцию
    y = func(x)

    inp1 = browser.find_element(By.ID, "answer")
    inp1.send_keys(y)

    sabmit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    sabmit.click()

finally:
    time.sleep(5)
    browser.quit()
