from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    browser = webdriver.Chrome()
    login = browser.find_element(By.CSS_SELECTOR, "[name=Login]")
    print("\nввод логина")
    login.send_keys("надо логин")

def password():
    browser = webdriver.Chrome()
    password = browser.find_element(By.CSS_SELECTOR, "[name=Password]")
    print("\nввод пароля")
    password.send_keys("надо пароль")
    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()

