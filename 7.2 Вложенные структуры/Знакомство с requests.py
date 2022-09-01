### Request и запросы

# Библиотека Requests предназначена для запросов к внешним ресурсам,
# у нее много возможностей, но пока нам интересны содержимое сайтов и получение данных в JSON.
#
# Вы можете установить библиотеку Requests, используя утилиту pip.

# pip install requests
# или
# pip3 install requests

# Чтобы выполнить запрос, напишите:
# import requests
# response = requests.get('адрес')

# Используйте метод JSON, чтобы превратить текст ответа в словарь или список:
# import requests
# response = requests.get('адрес')
# response_json = response.json()



# **Статус-коды**
#
# Не все запросы одинаково успешны. Иногда нам нужно обнаружить такой случай и
# обработать его — вывести ошибку и обработать запрос позже. Чтобы понять, выполнен ли
# запрос и передал ли сервер нужные данные, сервер отдает статус-код.
# Его можно посмотреть в поле status_code.

# import requests
# response = requests.get('https://catfact.ninja/fact')
#
# print(response.status_code)

# Статус-код — это целое число. Типичные значения статус-кодов:
#
# 200 — Ok.
# 404 — Страницы нет, и я вам ее не отдам.
# 403 — Страница есть, но я вам ее не отдам.
# 500 — Сервер поломался.
# 503 — Сервер долго не отвечает.





# import requests
#
# response = requests.get('https://api.ip2country.info/ip?55.53.53.5')
#
# print(response.status_code)





# import requests

# response = requests.get('https://catfact.ninja/fact')

# print(response)

# print(response.json())

# for fact in range(3):
#     response = requests.get('https://catfact.ninja/fact').json()
#     print(f"#{fact + 1} - {response['fact']}")
