import pytest
from selenium.webdriver.common.by import By
import time

# browser идет из contest.py

link = "https://stepik.org/lesson/236895/step/1"

def test_open_stepik(browser):
    browser.get(link)
    enter_form = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    enter_form.click()
    # time.sleep(100)

    login_enter = browser.find_element(By.ID, "id_login_email")
    login_enter.send_keys("___")
    
    password_enter = browser.find_element(By.ID, "id_login_password")
    password_enter.send_keys("___")

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # time.sleep(3)


# id_login_email
# id_login_password
# [type="submit]"