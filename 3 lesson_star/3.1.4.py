numb_str = input("Введите число прописью\n")

numb_list = numb_str.split(" ")

if len(numb_list) == 1:
	if numb_list[0] == "one":
		print("1")
	if numb_list[0] == "two":
		print("2")
	if numb_list[0] == "three":
		print("3")
	if numb_list[0] == "four":
		print("4")
	if numb_list[0] == "five":
		print("5")
	if numb_list[0] == "six":
		print("6")
	if numb_list[0] == "seven":
		print("7")
	if numb_list[0] == "eight":
		print("8")
	if numb_list[0] == "nine":
		print("9")
	if numb_list[0] == "ten":
		print("10")
	if numb_list[0] == "eleven":
		print("11")
	if numb_list[0] == "twelve":
		print("12")
	if numb_list[0] == "thirteen":
		print("13")
	if numb_list[0] == "fourteen":
		print("14")
	if numb_list[0] == "fifteen":
		print("15")
	if numb_list[0] == "sixteen":
		print("16")
	if numb_list[0] == "seventeen":
		print("17")
	if numb_list[0] == "eighteen":
		print("18")
	if numb_list[0] == "nineteen":
		print("19")
	if numb_list[0] == "twenty":
		print("20")
elif len(numb_list) == 2:
	if numb_list[0] == "twenty":
		print("2", end="")
	if numb_list[0] == "thirty":
		print("3", end="")
	if numb_list[0] == "forty":
		print("4", end="")
	if numb_list[0] == "fifty":
		print("5", end="")
	if numb_list[0] == "sixty":
		print("6", end="")
	if numb_list[0] == "seventy":
		print("7", end="")
	if numb_list[0] == "eighty":
		print("8", end="")
	if numb_list[0] == "ninety":
		print("9", end="")
	if numb_list[1] == "one":
		print("1")
	if numb_list[1] == "two":
		print("2")
	if numb_list[1] == "three":
		print("3")
	if numb_list[1] == "four":
		print("4")
	if numb_list[1] == "five":
		print("5")
	if numb_list[1] == "six":
		print("6")
	if numb_list[1] == "seven":
		print("7")
	if numb_list[1] == "eight":
		print("8")
	if numb_list[1] == "nine":
		print("9")
elif len(numb_list) > 2:
	print("Слишком большое число")
