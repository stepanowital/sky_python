from utils import load_random_word
from player import Player


if __name__ == '__main__':
	# Информация по словам на удаленном ресурсе
	data_words = "https://jsonkeeper.com/b/OYEP"

	# Запрос имени игрока и приветствие
	user_name = input("Введите имя игрока:\n")

	# Создание экземпляра класса Player
	player = Player(user_name)

	print(f"Привет, {player.user_name}!")

	# Присвоение слову выбор из случайного списка
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
			print("Это повторное слово")
		else:
			print("Красава")
			player.go_to_used_words(user_word)
		if len(player.used_words) == word_for_game.count_subwords():
			print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
			break
