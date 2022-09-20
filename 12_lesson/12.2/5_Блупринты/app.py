# app.py

# from flask import Flask
#
# # Импортируем блюпринты из их пакетов
# from catalog.views import catalog_blueprint
# from hello.profile import profile_blueprint
#
# app = Flask(__name__)
#
# # Регистрируем первый блюпринт
# app.register_blueprint(catalog_blueprint)
# # И второй тоже регистрируем
# app.register_blueprint(profile_blueprint)
#
# app.run()


# Делегирование URL и префиксы
# app.register_blueprint(messages_blueprint, url_prefix='/messages')


from flask import Flask

# Импортируем блюпринты из их пакетов
from messages.views import messages_blueprint

app = Flask(__name__)

# Регистрируем блюпринт c указанием префикса
app.register_blueprint(messages_blueprint, url_prefix='/messages')

app.run()
