from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

# запуск1 pytest -s -v "143auto_tests\stepik auto test\lesson3\lesson3-6_step6.py"

# запуск2 pytest -s -v --browser_name=firefox "143auto_tests\stepik auto test\lesson3\lesson3-6_step6.py" почему-то не работает
