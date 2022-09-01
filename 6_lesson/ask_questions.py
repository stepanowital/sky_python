import random


def ask_questions(words):
    """
    Открываем words.txt, берём оттуда слово, перемешиваем его буквы, выдаём пользователю в зашифрованном виде,
    считаем полученные очки
    """
    score = 0
    with open(words) as file:
        for word in file:
            if "\n" in word:
                word = word[0:len(word) - 1]
            word_list = []
            for letter in word:
                word_list += letter

            random.shuffle(word_list)

            word_shuffle = "".join(word_list)
            # for letter in word_list:
            #     word_shuffle += letter

            answer = input(f"\nУгадайте слово: {word_shuffle}\n")

            if answer == word:
                print("Верно! Вы получаете 10 очков.\n")
                score += 10
            else:
                print(f"Неверно! Верный ответ – {word}.")
    return score
