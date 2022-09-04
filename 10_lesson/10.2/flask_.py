# Например, функция page_index() будет обрабатывать запросы к адресу /index,
# функция page_catalog() будет обрабатывать запросы к адресу /catalog и так далее!


# Flask включает в себя компоненты для работы:
#
# с маршрутами и методами,
# статическими файлами,
# загрузкой файлов
# шаблонами,
# cookies и сессиями,
# ошибками,
# JSON-данными,
# тестами,
# промежуточным слоем WSGI.

# Flask не включает в себя, но может быть расширен для работы:
#
# с базой данных,
# инструментами обработки форм,
# инструментами контроля доступа,
# инструментами кеширования,
# админкой,
# инструментами отладки,
# очередями.



from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Мурка, я тебя люблю"

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route("/test/")
def page_test():
    return "Приложение работает"

@app.route('/users/<int:uid>')
def page_users(uid):
   return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/items/<int:itemid>')
def page_items(itemid):
   return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='0.0.0.0', port=8000)
# app.run(host='127.0.0.2', port=80)
app.run()