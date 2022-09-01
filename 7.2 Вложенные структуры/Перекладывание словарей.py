# user_info_1 = {"name": "Алексей", "surname": "Алишевский", "age": "35"}
#
# # user_info_2 = {"i": "Алексей", "f": "Алишевский", "yo": "35"}
#
# user_info_2 = {"i": user_info_1["name"], "f": user_info_1["surname"], "yo": user_info_1["age"]}
#
# print(user_info_2)





# Для получения значения ключи пишутся последовательно в квадратных скобках.

# dictionary["outerkey"]["innerkey"]



# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# print(store["apples"]["name"])
# print(store["oranges"]["available"])



# **Вывод в цикле**
#
# Если мы хотим использовать цикл, можно использовать items():

# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# for item in store.values():
#   print(item["name"], item["price"])



# А можно использовать ключи:

# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# for key in store:
#   print(store[key]["name"], store[key]["price"])




