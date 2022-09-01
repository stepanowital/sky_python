class Player:

	def __repr__(self):
		return "Я тут самый главный"

	def __init__(self, user_name):
		self.user_name = user_name
		self.used_words = []

	def count_used_words(self):
		"""
		Получение количества использованных слов
		"""
		return len(self.used_words)

	def go_to_used_words(self, user_word):
		"""
		Добавление слова в использованные слова
		"""
		self.used_words.append(user_word)

	def check_used_words(self, user_word):
		"""
		Проверка использования данного слова до этого
		"""
		if user_word in self.used_words:
			return True
		return False
