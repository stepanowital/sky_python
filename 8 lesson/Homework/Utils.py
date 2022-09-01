class Question:

	def __init__(self, text, complexity, correct_answer):
		self.text = text
		self.complexity = complexity
		self.correct_answer = correct_answer

		self.is_ask = False
		self.user_answer = None
		self.points = int(self.complexity) * 10

	def get_points(self):
		"""
		Возвращает int, количество баллов.
		Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
		"""
		return self.points

	def is_correct(self):
		"""
		Возвращает True, если ответ пользователя совпадает
		с верным ответов иначе False.
		"""
		if self.correct_answer == self.user_answer:
			return True
		else:
			return False

	def build_question(self):
		"""
		Возвращает вопрос в понятном пользователю виде, например:
		Вопрос: What do people often call American flag?
		Сложность 4/5
		"""
		return f"Вопрос: {self.text}\nСложность {self.complexity}/5"

	def build_feedback(self):
		"""
		Возвращает :
		Ответ верный, получено __ баллов
		или
		Ответ неверный, верный ответ __
		"""
		if self.is_correct():
			return f"Ответ верный, получено {self.points} баллов\n"
		return f"Ответ неверный, верный ответ {self.correct_answer}\n"


def get_statistics(questions):
	"""
	Вот и всё!
	Отвечено _ вопроса из __
	Набрано баллов: ___
	"""
	score = 0
	count = 0

	for question in questions:
		if question.is_correct():
			score += question.points
			count += 1
	return f"Вот и всё!\n" \
		   f"Отвечено на {count} вопрос(а,ов) из 5\n" \
		   f"Набрано баллов: {score}"
