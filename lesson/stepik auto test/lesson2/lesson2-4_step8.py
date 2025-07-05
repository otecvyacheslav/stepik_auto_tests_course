import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def math1(x):  # указываем имя функции и ожидаемый элемент для функции
    return str(
        math.log(abs(12 * math.sin(int(x))))
    )  # здесь мы данный элемент кидаем в функцию


browser = webdriver.Chrome()  # запуск хромдрайв
browser.get("https://suninjuly.github.io/explicit_wait2.html")  # переход по ссылке


sell_price = WebDriverWait(browser, 15).until(  # использую ожидание до 15 секунд
    EC.text_to_be_present_in_element(
        (By.ID, "price"), "$100"
    )  # пока не появится элемент $100 в необходимом ID
)


book = browser.find_element(By.ID, "book")  # простой поиск кнопки
book.click()  # и клик кнопки, там как выполнение идет последовательно, то оно произошло после найденного элемента вверху

x_find = browser.find_element(By.ID, "input_value")  # поиск значения Х в тексте
x = x_find.text  # вытащили текст
y = math1(x)  # задали переменную для Х и выщвали функцию, чтобы ее посчитать

input1 = browser.find_element(By.ID, "answer")  # нашли куда вводить
input1.send_keys(y)  # ввели посчитанное

enter = browser.find_element(By.ID, "solve")  # нашли кнопку
enter.click()  # нажали

time.sleep(10)  # ждем 10 сек, чтобы скопировать полученный код
browser.quit  # закрыли браузер

# ниже поля из страницы, чтобы не искать на ней в моменте, а сразу выбрать из представленного
# ++

# <span class="nowrap" id="input_value">660</span> 1111

# input <input class="form-control" name="text" id="answer" type="text" required="">

# enter <button id="solve" type="submit" class="btn btn-primary" disabled="disabled">Submit</button>

# хочу добавить изменение в файл, чтобы оно появилось в гите
