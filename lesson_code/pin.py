def check_pin(pin):
    """
    Проверка длины пин-кода
    """
    pin_str = str(pin)
    if len(pin_str) == 4 and pin_str.isdigit():
        return True
    else:
        return False


# try:
#     assert check_pin("1234") == True
#     assert check_pin("123") == False
#     assert check_pin("a000") == False
#     assert check_pin("0000") == True
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")

