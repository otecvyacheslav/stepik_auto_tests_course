def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"excepted {expected_result}, got {actual_result}"
# в функции реализуем вывод ошибки, если 1 значение не равно 2. Также в f-string выводим еще и дополнительный текст с объяснением почему

test_input_text(1, 11) # это применение функции, указанной выше
