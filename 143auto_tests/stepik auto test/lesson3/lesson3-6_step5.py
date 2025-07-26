import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from asd import login_stepik
from asd import password_stepik
import math

answer = math.log(int(time.time() + 0.2))

# browser идет из conftest.py
# логин и пароль хранится отдельно


@pytest.mark.parametrize(
    "links",
    [
        "https://stepik.org/lesson/236895/step/1",
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
    # time.sleep(3)

    
    print("очистка поля ввода")
    time.sleep(100)
    browser.find_element(By.CLASS_NAME, "ember-text-area").clear()

    print("ввод вычисленного значения из указанного времени")
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(str(answer))
    # time.sleep(5)

    print("нажатие на отправить, вот тут идет ожидание, пока кнопка станет доступна")
    send_answer = browser.find_element(By.CLASS_NAME, "submit-submission")

    # WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    # )

    send_answer.click()
    time.sleep(5)

    print("проверяю полученный ответ, равен ли он ожиданию")
    message = browser.find_element(By.CSS_SELECTOR, "#ember541 > p")
    # text_in_message = message.text

    print("прям перед ассертом")
    rly_text = "Correct!"

    assert message == rly_text, f"Сообщение в {message} не содержит Correct!"


# <button class="again-btn white" type="button" data-ember-action="" data-ember-action-555="555">
#                   Решить снова
# <!---->                </button>