class BasicWord:

	def __init__(self, word, subwords):
		self.word = word
		self.subwords = subwords

	def __repr__(self):
		return f"{self.word.title()}"

	def check_word(self, user_word):
		"""
		Проверка введенного слова в списке допустимых подслов
		"""
		is_real = False
		for word in self.subwords:
			if user_word == word:
				is_real = True
		return is_real

	def count_subwords(self):
		"""
		Подсчет количества подслов
		"""
		return len(self.subwords)
