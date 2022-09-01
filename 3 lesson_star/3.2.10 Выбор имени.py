serbian = [
	"Никола", "Лука", "Стефан", "Марко", "Лазар", "Александр",
	"Филип", "Йован", "Неманя", "Милош", "Душан"]

kazakh = ["Муртаза", "Меджит", "Ильяс", "Харун", "Нурадил", "Айрат", "Айрат", "Азиль", "Ерлан"]

yakutian = ["Айхал", "Эркин", "Хорула", "Уруй", "Дуолан", "Дохсун", "Тимир"]

baby_name = None

for name in serbian:
	print(f"Как вам имя {name}? (да/нет)")
	user_answer = None
	while user_answer not in ["да", "нет"]:
		user_answer = input()
		if user_answer == "нет":
			continue
		elif user_answer == "да":
			print(
				"Отлично, вот мы и выбрали имя. "
				"Я пойду :)")
			quit()
		else:
			print("Попробуйте еще раз ввести ответ (да или нет)")

print("\nСербские имена закончились. Переходим к казахским!")

for name in kazakh:
	print(f"Как вам имя {name}? (да/нет)")
	user_answer = None
	while user_answer not in ["да", "нет"]:
		user_answer = input()
		if user_answer == "нет":
			continue
		elif user_answer == "да":
			print(
				"Отлично, вот мы и выбрали имя. "
				"Я пойду :)")
			quit()
		else:
			print("Попробуйте еще раз ввести ответ (да или нет)")

print("\nКазахские имена закончились. Переходим к якутским!")

for name in yakutian:
	print(f"Как вам имя {name}? (да/нет)")
	user_answer = None
	while user_answer not in ["да", "нет"]:
		user_answer = input()
		if user_answer == "нет":
			continue
		elif user_answer == "да":
			print(
				"Отлично, вот мы и выбрали имя. "
				"Я пойду :)")
			quit()
		else:
			print("Попробуйте еще раз ввести ответ (да или нет)")

print("\nУ меня закончились варианты, назовите его новый_сын_1")