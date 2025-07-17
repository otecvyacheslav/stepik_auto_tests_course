# функция проверяет есть ли текст в указанном тексте
def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert (
        substring in full_string
    ), f"expected '{substring}' to be substring of '{full_string}'"


test_substring("1", "1")
