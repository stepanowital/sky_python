from ask_questions import ask_questions
from save_to_history import save_to_history
from statistics import get_statistics

words = "words.txt"
history = "history.txt"

user_name = input("Введите ваше имя:\n")

# Открываем words.txt, берём оттуда слово, перемешиваем его буквы и выдаём пользователю в зашифрованном виде
score = ask_questions(words)

# Добавляем в history.txt Имя и очки пользователя
save_to_history(history, user_name, score)

# Открываем history.txt считаем кол-во сыгранных игр и максимальный счёт
print(get_statistics(history))
