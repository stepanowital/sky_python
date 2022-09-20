print("строка 1")
print("строка 2")
print("строка 3")
print("строка 4")
print("строка 5")


# def my_max(items):
#   current_max = items[0]
#
#   for index in range(1, len(items)):
#     item = items[index]
#     if item > current_max:
#       current_max = item
#
#   return current_max
#
# the_max = my_max([99, 1, 0, -99, -1, 105])
# print(the_max)


# a = True
#
# if a:
# 	print("Значение Истина")
# else:
# 	print("Значение Ложь")
#
#
# numbers = ["ноль", "один", "два", "три", "четыре", "пять"]
# index = 5
#
# # измените значение index здесь
#
# if 0 <= index <= 5:
# 	print(numbers[index])

# a = 1
# print(a)
# a = 2
# print(a)
# a = 3
# print(a)
# a = 4
# print(a)
# a = 5
# print(a)
# a = 6
# print(a)


# a = 1
# b = 2
# c = 3
#
# a = 4
# b = 5
# c = 6
#
# del a
# del b
# del c


# a = 2**2+2**2**2+2**2
#
# a *= 2
#
# a *= a
#
# print(a)



# line = "В аквариуме у Харитона четыре рака да три тритона."
#
# line.replace("р", "")
#
# count = line.count("р")
#
# a = 10


# class NotInRangeError(Exception):
#
# 	pass
#
#
# def verbose_grade(grade_int):
#
#     if grade_int == 2:
#         return "Плохо"
#     elif grade_int == 3:
#         return "Плохо"
#     elif grade_int == 4:
#         return "Хорошо"
#     elif grade_int == 5:
#         return "Отлично"
#
#     raise NotInRangeError("Value from 2 to 5 expected")
#
# # И сразу же вызовем ее
#
# verbose_grade(1)


# grade_int = 8
#
#
# class NotInRangeError(Exception):
#
#     def __init__(self, message=None):
#         super().__init__(message)
#
#
# def verbose_grade(grade_int):
#
#     if grade_int == 2:
#         return "Плохо"
#     elif grade_int == 3:
#         return "Плохо"
#     elif grade_int == 4:
#         return "Хорошо"
#     elif grade_int == 5:
#         return "Отлично"
#
#     raise NotInRangeError("Value from 2 to 5 expected")
#
# # И сразу же вызовем с неверными данными
#
# try:
#     verbose_grade(6)
# except NotInRangeError:
#     print("Значение вне диапазона разрешенных значений")


def verbose_month(month_number):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    if month_number < 1 or month_number > 12:
        raise ValueError("1 to 12 Expected")
    return months[month_number - 1]

print(verbose_month(122))