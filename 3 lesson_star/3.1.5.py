numb = input("Введите положительное число\n")

if len(numb) == 2:
	numb_list = [numb[0], numb[1]]

	if numb_list[0] == "1":
		if numb_list[1] == "0":
			print("десять")
		if numb_list[1] == "1":
			print("одиннадцать")
		if numb_list[1] == "2":
			print("двенадцать")
		if numb_list[1] == "3":
			print("тринадцать")
		if numb_list[1] == "4":
			print("четырнадцать")
		if numb_list[1] == "5":
			print("пятнадцать")
		if numb_list[1] == "6":
			print("шестнадцать")
		if numb_list[1] == "7":
			print("семнадцать")
		if numb_list[1] == "8":
			print("восемнадцать")
		if numb_list[1] == "9":
			print("девятнадцать")
		quit()

	if numb_list[0] == "2":
		print("двадцать", end=" ")
	if numb_list[0] == "3":
		print("тридцать", end=" ")
	if numb_list[0] == "4":
		print("сорок", end=" ")
	if numb_list[0] == "5":
		print("пятьдесят", end=" ")
	if numb_list[0] == "6":
		print("шестьдесят", end=" ")
	if numb_list[0] == "7":
		print("семьдесят", end=" ")
	if numb_list[0] == "8":
		print("восемьдесят", end=" ")
	if numb_list[0] == "9":
		print("девяносто", end=" ")

	if numb_list[1] == "1":
		print("один")
	if numb_list[1] == "2":
		print("два")
	if numb_list[1] == "3":
		print("три")
	if numb_list[1] == "4":
		print("четыре")
	if numb_list[1] == "5":
		print("пять")
	if numb_list[1] == "6":
		print("шесть")
	if numb_list[1] == "7":
		print("семь")
	if numb_list[1] == "8":
		print("восемь")
	if numb_list[1] == "9":
		print("девять")

elif len(numb) == 1:
	numb_list = [numb[0]]

	if numb_list[0] == "0":
		print("ноль")
	if numb_list[0] == "1":
		print("один")
	if numb_list[0] == "2":
		print("два")
	if numb_list[0] == "3":
		print("три")
	if numb_list[0] == "4":
		print("четыре")
	if numb_list[0] == "5":
		print("пять")
	if numb_list[0] == "6":
		print("шесть")
	if numb_list[0] == "7":
		print("семь")
	if numb_list[0] == "8":
		print("восемь")
	if numb_list[0] == "9":
		print("девять")

elif len(numb) > 2:
	print("Слишком длинное число")
