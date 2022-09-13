import json


def load_candidates(data_source):
	"""
	Загружает данные из файла
	"""
	with open(data_source, 'r', encoding="utf-8") as file:
		return json.load(file)


def get_all(candidates):
	"""
	Показывает всех кандидатов
	"""
	result = "<br>"
	for candidate in candidates:
		result += "Имя кандидата - " + candidate['name'] + "<br>"
		result += "Позиция кандидата: " + candidate['position'] + "<br>"
		result += "Навыки через запятую: " + candidate['skills'] + "<br>"
		result += "<br>"
	return f"<pre> {result} </pre>"


def get_by_pk(candidates, pk):
	"""
	Возвращает кандидата по pk
	"""
	if 0 < pk <= 7:
		candidate = candidates[pk-1]

		result = "<br>"
		result += "Имя кандидата - " + candidate['name'] + "<br>"
		result += "Позиция кандидата: " + candidate['position'] + "<br>"
		result += "Навыки через запятую: " + candidate['skills'] + "<br>"
		result += "<br>"
		return f"""
			<img src="{candidate['picture']}">
			<pre> {result} </pre>
			"""
	else:
		return f"<pre> Кандидат не найден </pre>"


def get_by_skill(candidates, skill):
	"""
	Возвращает кандидата по навыку
	"""

	result = "<br>"
	for candidate in candidates:
		if skill.lower() in candidate['skills'].lower().split(", "):
			result += "<br>"
			result += "Имя кандидата - " + candidate['name'] + "<br>"
			result += "Позиция кандидата: " + candidate['position'] + "<br>"
			result += "Навыки через запятую: " + candidate['skills'] + "<br>"
			result += "<br>"
	if result == "<br>":
		return f"<pre> Кандидат не найден </pre>"
	else:
		return f"<pre> {result} </pre>"
