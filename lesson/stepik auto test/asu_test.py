from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://erp.solforb.ru/Testvv/ASUReact/login"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    login = browser.find_element(By.CSS_SELECTOR, "[name=Login]")
    login.send_keys("support")
    password = browser.find_element(By.CSS_SELECTOR, "[name=Password]")
    password.send_keys("Solforb.2015")

    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()

    # menu = browser.find_element(By.CSS_SELECTOR, "dropdown-toggle")
    # menu.click()

    time.sleep(2)

finally:
    time.sleep(5)
    browser.quit()
