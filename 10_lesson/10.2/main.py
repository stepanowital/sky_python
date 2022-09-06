# PIP позволяет получать список всех зависимости проекта при помощи команды:
#
# $ pip freeze


# PIP позволяет фиксировать все зависимости проекта в одном файле requirements.txt при помощи этой команды:
#
# $ pip freeze > requirements.txt

# pip install flask


# Зависимости проекта — список пакетов, необходимых для его работы,
# обычно с указанием версий каждого пакета.

# Менеджер пакетов (менеджер зависимостей) — ПО (чаще всего консольное) для установки,
# обновления и удаления программ.


# Мы последовали совету и составили список зависимостей.
# Открыли проект на новом месте и готовы устанавливать зависимости.
# Что делать? Прописываем эту строку:
#
# pip install -r requirements.txt
#
# Если в нашем списке зависимостей pytest (пакет для тестирования нашего приложения),
# flake8 (инструмент для улучшения качества кода) black (еще один инструмент для улучшения
# качества кода), то такая команда — то же самое, что написать:
#
# pip install pytest flake8 black


# Шаг 0. Установка модуля venv
# В MacOS и Windows этот модуль, как и PIP, входит в поставку Python.
# На Ubuntu его нужно установить отдельно командой:
# sudo apt install python3-venv


# Шаг 1. Создание окружения
# Создается окружение командой:
# python3 -m venv имя_окружения
# # Обычно это
# python -m venv venv


# Шаг 2. Активация виртуального окружения
# Когда мы создаем окружение командой из прошлого пункта, в папке bin появляется
# скрипт активации, который на MacOS и Ubuntu называется activate, а на Windows — activate.bat. Нам нужно его запустить.
# На MacOS и Ubuntu вызвать команду:
# source <название_окружения>/bin/activate
# $source venv/bin/activate
#
# На Windows вызвать команду:
# C:\> <название_окружения>\Scripts\activate.bat
# C:\> venv\Scripts\activate.bat
#
# Если ваша Windows использует Power Shell:
#
# C:\> <название_окружения>\Scripts\activate.ps1
# C:\> venv\Scripts\activate.ps1

from flask_ import *

# def hello():
# 	return 'Hello World'
#
# if __name__ == '__main__':
# 	print(hello())
# else:
# 	print("Это не мой мир")

# Ответ на вопрос, который мы задавали в начале будет таким:
# такая конструкция помогает поймать сразу 2 зайцев – стартовать
# тестовый веб-сервер при запуске напрямую и не стартовать при импортировании.