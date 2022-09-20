# import logging
#
# from flask import Flask
#
# # add filemode="w" to overwrite
# logging.basicConfig(level=logging.INFO)
#
# app = Flask(__name__)
#
#
# @app.route('/',)
# def page_index():
#     logging.info("Главная страница запрошена")
#     return "Главная страница"
#
#
# @app.route('/store')
# def page_store():
#     logging.info("Страница магазина запрошена")
#     return "Страница магазина "
#
#
# @app.route('/store/<cat>')
# def page_cat(cat):
#     logging.info(f"Страница категории {cat} запрошена")
#     return f"Страница категории {cat} "
#
#
# app.run()









# import logging
#
# from flask import Flask, request, render_template
#
# # Добавили файл, в который пишем логи
# logging.basicConfig(filename="basic.log", level=logging.INFO)
#
# app = Flask(__name__)
#
#
# @app.route('/',)
# def page_index():
#     logging.info("Главная страница запрошена")
#     return "Главная страница"
#
#
# @app.route('/store')
# def page_store():
#     logging.info("Страница магазина запрошена")
#     return "Страница магазина "
#
#
# @app.route('/store/<cat>')
# def page_cat(cat):
#     logging.info(f"Страница категории {cat} запрошена")
#     return f"Страница категории {cat} "
#
#
# app.run()



#
#
# import logging
#
#
# logger_one = logging.getLogger("one")
# logger_two = logging.getLogger("two")
#
# logger_one.warning("Логгер первый работает")
# logger_one.warning("Логгер второй работает")
#





# import logging
#
# logger_one = logging.getLogger("one")
# logger_two = logging.getLogger("two")
#
# file_handler_one = logging.FileHandler("log_one.txt")
# file_handler_two = logging.FileHandler("log_two.txt")
#
# logger_one.addHandler(file_handler_one)
# logger_two.addHandler(file_handler_two)
#
# logger_one.warning("Запись для логгера один")
# logger_two.warning("Запись для логгера два")




# import logging
#
# new_logger = logging.getLogger()
#
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("log.txt")
#
# new_logger.addHandler(console_handler)
# new_logger.addHandler(file_handler)
#
# new_logger.warning("Все работает")




# import logging
#
# # Создаем или получаем новый логгер
# logger_one = logging.getLogger("one")
#
# # Cоздаем ему обработчик
# console_handler = logging.StreamHandler()
#
# # Создаем новое форматирование (объект класса Formatter)
# formatter_one = logging.Formatter("%(asctime)s : %(message)s")
#
# # Применяем форматирование к обработчику
# console_handler.setFormatter(formatter_one)
#
# # Добавляем обработчик к журналу
# logger_one.addHandler(console_handler)
#
# logger_one.warning("Логгер первый работает")





# name = "Алиса"
# logging.info(f"Пользователь {name} пытается войти")
# logging.warning(f"Пользователь {name} проблемы с оплатой")
# logging.critical(f"Пользователь {name} все сломал")




# import logging
# import json
# from json import JSONDecodeError
#
# logging.basicConfig(filename="basic.log")
#
# try:
#     path = "data.json"
#     file = open(path)
#     items = json.load(file)
#     for item in items:
#         print(item)
# except FileNotFoundError:
#     logging.exception("Ошибка доступа к файлу")
#
# except JSONDecodeError:
#     # Будет выполнено если файл найден, но не превращается из JSON
#     logging.exception("Файл не удается преобразовать")




import logging

from flask import Flask

# add filemode="w" to overwrite
logging.basicConfig(filename="basic.log")

app = Flask(__name__)

@app.route('/',)
def page_index():
    return "Главная страница"

@app.route('/store')
def page_store():
    return "Страница магазина "

@app.route('/store/<cat>')
def page_cat(cat):
    return f"Страница категории {cat} "

app.run()