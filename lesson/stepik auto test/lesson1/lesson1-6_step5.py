import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/find_link_text")

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(a)

link = browser.find_element(By.LINK_TEXT, a)
link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Vyacheslav")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Voropaev")
input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("Lipetsk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(15)

browser.quit()
