

ticket_numb = input("Введите номер билетика\n")
if len(ticket_numb) != 6:
	print("Не хватает цифр на билетике, возможно, вы уже съели часть?")
	quit()
ticket_list = [
	int(ticket_numb[0]),
	int(ticket_numb[1]),
	int(ticket_numb[2]),
	int(ticket_numb[3]),
	int(ticket_numb[4]),
	int(ticket_numb[5])
]
if sum(ticket_list[:3]) == sum(ticket_list[3:]):
	print("Это счастливый билетик, ешьте его скорей!")
else:
	print("Это обычный билетик, но вы все равно можете его съесть!")
