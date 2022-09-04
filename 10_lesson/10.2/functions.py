# def hello():
#     print("hello")
#
# def wrap(another_func):
#     print("Я получаю функцию и возвращаю, как есть")
#     return another_func
#
# new_hello = wrap(hello)
# new_hello()
#
# # Будет работать и выводить
# # Я получаю функцию и возвращаю, как есть
# # hello




# def function_1():
#     print("hello")
#
# def function_2():
#     print("bye")
#
# funcs = [function_1, function_2]
# funcs[0]()
# funcs[1]()
#
# # Будет работать и выводить
# # hello
# # bye




# registered = {}
#
# def hello():
#     """ Изначальная функция """
#     print("hello")
#
#
# def register_func(another_func, name):
#     """ Функция регистрации в словаре"""
#     registered[name] = another_func
#
# register_func(hello, "Поздороваться")
# print(registered)
#
# # Выведет
#
# # {'Поздороваться': }




# registered = {}
#
# def func_1():
#     print("Давай начнем")
#
# def func_2():
#     print("Давай закончим")
#
# def register_func(another_func, name):
#     registered[name] = another_func
#
# register_func(func_1, "start")
# register_func(func_2, "end")
#
# user_input = input("Введите команду")
# function_to_call = registered.get(user_input)
# function_to_call()
#
# # Программа: Введите команду
# # Пользователь: start
# # Программа: Давай начнем
#
# # Программа: Введите команду
# # Пользователь: end
# # Программа: Давай закончим




# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def page_test():
#      return "Ваше первое приложение"





# def hello():
#     """ изначальная функция """
#     print("hello")
#
# def angry_func():
#     """ новая функция """
#     print("grrrht!")
#
# def wrap(another_func):
#     """ функция, превращающая одну в другую """
#     print("Я получаю функцию и делаю ее злой")
#     return angry_func
#
# hello = wrap(hello)
# hello()
#
#  # Вернет
#
#  # Я получаю функцию и делаю ее злой
#  # grrrht!


#
#
# def hello():
#     """ изначальная функция """
#     print("hello")
#
# def angry_func():
#     """ новая функция """
#     print("Это опять ты!")
#     hello()
#     print("Я разрушу всё, что ты создашь!")
#
# def wrap(another_func):
#     """ функция, превращающая одну в другую """
#     print("Я получаю функцию и делаю ее злой")
#     return angry_func
#
# new_hello = wrap(hello)
# new_hello()

 # Выведет

 # Я получаю функцию и делаю ее злой
 # Это опять ты!
 # hello
 # Я разрушу всё, что ты создашь!





#               ДЕКОРАТОРЫ
# @decorate
# def another_function():
#     print("Я делаю работу")

# Такая запись означает, что функция another_function будет
# передана функции @decorate, функция @decorate получите ее,
# что-то с ней сделает, а результат, который функция-декоратор вернет,
# будет называться another_function.


# def log(func):
#    def wrapper():
#        print("Я слежу за тобой, функция!")
#        func()
#    return wrapper
#
# @log
# def another_function():
#    print("Что-то выполняется")
#
# another_function()
#
#  # Выведет:
#
#  # Я слежу за тобой, функция!
#  # Что-то выполняется



# @check_access
# def another_function():
#    print("Что-то выполняется")
# Такая запись означает, что функция another_function будет декорирована
# функцией check_access. На практике это, скорее всего, значит, что
# до кода тела функции будет выполнена некоторая проверка и код тела
# функции будет выполнен, только если у текущего пользователя есть права
# на выполнение.Код декорирующей функции check_access приводить не будем.




# @convert_to_json
# def another_function():
#    return {"key": "value"}
# Такая запись означает, что функция another_function будет декорирована
# функцией convert_to_json. На практике это, скорее всего, значит, что
# результат выполнения функции будет превращен в JSON c помощью библиотеки
# JSON.Код декорирующей функции convert_to_json мы приводить не будем.




# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def page_test():
#      return "Ваше первое приложение"
#
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
# def page_test():
#      return "Ваше первое приложение"
#
# app.add_url_rule('/', view_func=page_index)
