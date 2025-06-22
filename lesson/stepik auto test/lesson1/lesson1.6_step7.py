from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("XPATH.Vyacheslav")
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("XPATH.Voropaev")
    input3 = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control') and contains(@class, 'city')]")
    input3.send_keys("XPATH.Lipetsk")
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("XPATH.Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла