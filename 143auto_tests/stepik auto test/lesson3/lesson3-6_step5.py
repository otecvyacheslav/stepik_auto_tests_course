import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from asd import login_stepik
from asd import password_stepik
import math

answer = math.log(int(time.time() + 1))

# browser идет из conftest.py
# логин и пароль хранится отдельно


@pytest.mark.parametrize(
    "links",
    [
        "https://stepik.org/lesson/236895/step/1"
        # "https://stepik.org/lesson/236896/step/1",
        # "https://stepik.org/lesson/236897/step/1",
        # "https://stepik.org/lesson/236898/step/1",
        # "https://stepik.org/lesson/236899/step/1",
        # "https://stepik.org/lesson/236903/step/1",
        # "https://stepik.org/lesson/236904/step/1",
        # "https://stepik.org/lesson/236905/step/1",
    ],
)
def test_open_stepik(browser, links):
    print("переход по ссылке")
    link = f"{links}"
    browser.get(link)
    enter_lk = browser.find_element(
        By.CSS_SELECTOR,
        ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button",
    )
    enter_lk.click()

    print("ввод логина")
    login_enter = browser.find_element(By.ID, "id_login_email")
    login_enter.send_keys(login_stepik)

    print("ввод пароля")
    password_enter = browser.find_element(By.ID, "id_login_password")
    password_enter.send_keys(password_stepik)

    print("нажатие на вход в аккаунт")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(3)

    print("очистка поля ввода")
    browser.find_element(By.CLASS_NAME, "ember-text-area").clear()

    time.sleep(1)
    print("ввод вычисленного значения из указанного времени")
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)

    print("нажатие на отправить, вот тут идет ожидание, пока кнопка станет доступна")
    send_answer = browser.find_element(By.CLASS_NAME, "submit-submission")

    # WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    # )

    send_answer.click()

    print("проверяю полученный ответ, равен ли он ожиданию")
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    text_in_message = message.text

    print("прям перед ассертом")
    time.sleep(15)

    assert (
        text_in_message == "Correct!"
    ), f"Сообщение в {text_in_message} не содержит Correct!"
