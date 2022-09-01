# ### **Формат JSON**
#
# Формат JSON — самый популярный текстовый формат во всем интернете.
#
# - Текстовый формат.
# - Структурированный.
# - Похож на словари в Python.
# - Можно хранить в файлах.
#
### Отличия от словарей в Python:

# Ключом может быть только строка.
# Всегда используются двойные кавычки.
# true пишется с маленькой буквы.
# После последнего элемента не ставится запятая.
# Нельзя использовать кортежи и множества — только списки и словари.
# Пустое значение не None, а null.



# Распаковка из JSON
# import json
#
# raw_json = '{ "name":"Алиса", "is_online":true }'
#
# profile = json.loads(raw_json)
#
# print(profile)


# Упаковка в JSON
# import json
#
# profile = {'name': 'Alice', 'is_online': True}
# json_string = json.dumps(profile)
#
# print(json_string)



# **Упаковка и распаковка в файлы**
#
# Загрузка из файла:
# import json
# file = open("example.json")
# json.load(file)


# Запись в файл:
# import json
# file = open("example.json", "a")
# data = ["mydata"]
# json.dump(data, file)
