from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    name1.send_keys("Nikita")

    name2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    name2.send_keys("Voropaev")

    email1 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    email1.send_keys("123@123.ew")

    # вставка поиска нахождения файла
    file_place1 = os.path.abspath(
        os.path.dirname(__file__)
    )  # переменная == искомое место файла
    files1 = os.path.join(file_place1, "primer.txt")  # переменная == ищем файл по имени

    import_form = browser.find_element(By.CSS_SELECTOR, "[name=file]")
    import_form.send_keys(files1)  # в скобках та переменная, что укажем во вставке

    button1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button1.click()


finally:
    time.sleep(3)
    browser.quit()
