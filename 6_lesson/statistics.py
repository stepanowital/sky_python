def get_statistics(history):
    """
    Открываем history.txt считаем кол-во сыгранных игр и максимальный счёт
    """
    with open(history, encoding="utf-8") as file:
        games_count = 0
        max_score = 0
        for line in file:
            games_count += 1
            actual_score_int = int(line.split(" ")[1])

            if actual_score_int > max_score:
                max_score = actual_score_int

    return f"\nВсего игр сыграно: {games_count}" \
           f"\nМаксимальный рекорд: {max_score}"
