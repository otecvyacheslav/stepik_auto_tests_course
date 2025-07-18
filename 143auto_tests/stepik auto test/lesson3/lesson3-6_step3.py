import pytest
from selenium.webdriver.common.by import By

# browser идет из contest.py


@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
