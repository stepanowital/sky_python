import requests
import random
from basic_word import BasicWord


def load_random_word(data_words):
	"""
	Получит список слов с внешнего ресурса,
	выберет случайное слово,
	создаст экземпляр класса `BasicWord`,
	вернет этот экземпляр.
	"""
	response = requests.get(data_words)
	response_json = response.json()

	random.shuffle(response_json)

	word = response_json[0]['word']
	subwords = response_json[0]['subwords']

	mainword = BasicWord(word, subwords)
	return mainword
