# from functions import imported_hello

# imported_hello()


# import functions

# functions.imported_hello()


# from functions import *

# imported_hello()

from pin import check_pin

print("Введите ваш ПИН-код")
user_input = input()

if check_pin(user_input):
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")
