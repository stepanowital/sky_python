if __name__ == '__main__':
	from utils import load_random_word
	from player import Player

	# Информация по словам на удаленном ресурсе
	data_words = "https://jsonkeeper.com/b/OYEP"

	# Запрос имени игрока и приветствие
	user_name = input("Введите имя игрока:\n")
	print(f"Привет, {user_name}!")

	# Добавление игрока к классу Player
	player = Player(user_name)

	# Присвоение слову выбор из случаного списка
	word_for_game = load_random_word(data_words)

	print(f"\nСоставьте {word_for_game.count_subwords()} слов из слова {word_for_game}")
	print("Слова должны быть не короче 3 букв")
	print('Чтобы закончить игру, угадайте все слова или напишите "stop"/"стоп"\n')

	print("Поехали, ваше первое слово?")
	while True:
		user_word = input().lower()
		if user_word == "стоп" or user_word == "stop":
			print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
			break
		if len(user_word) < 3:
			print("слишком короткое слово")
			continue
		if not word_for_game.check_word(user_word):
			print("Это неудачное слово")
			continue
		if player.check_used_words(user_word):
			print("Это неудачное слово")
		else:
			print("Красава")
			player.go_to_used_words(user_word)
			print(player.used_words)
		if len(player.used_words) == word_for_game.count_subwords():
			print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
			break
