# Начало работы с датой
# from datetime import date
#
# date_one = date(1815, 12, 12) # 12 декабря 1815
#
# print(date_one)


# Создаем время
# from datetime import time
#
# time_one = time(16, 20, 00) # 16 часов 20 минут
#
# print(time_one)


# Создаем время с датой
# from datetime import datetime
#
# datetime_one = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47
#
# print(datetime_one)



# Работа с объектом даты
# from datetime import datetime
#
# thedate = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47
#
# print("Год", thedate.year)
# print("Месяц", thedate.month)
# print("День", thedate.day)
# print("Час", thedate.hour)
# print("Минута", thedate.minute)
# print("Секунда", thedate.second)

# from datetime import date
#
# thedate = date(1970, 1, 5)
#
# print(thedate.weekday())


# Работа с текущей датой
# from datetime import datetime
#
# thedate = datetime.now()
#
# print(thedate)


# Получение даты из строки
# from datetime import date
#
# thedate = date.fromisoformat("2021-05-04")
#
# print(thedate.year)
# print(thedate.month)
# print(thedate.day)

# Пример со временем:
# from datetime import time
#
# thetime = time.fromisoformat("23:14")
#
# print(thetime.hour)
# print(thetime.minute)


# Пример с датой и временем:
# from datetime import datetime
#
# thedate = datetime.fromisoformat("2020-12-06 23:14")
#
# print(thedate.year)
# print(thedate.month)
# print(thedate.day)
#
# print(thedate.hour)
# print(thedate.minute)


from datetime import date

thedate = date(1970, 1, 5)

date_formatted = thedate.strftime("%d %B %Y ") # День Месяц Год

print(date_formatted)
