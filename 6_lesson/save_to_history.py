def save_to_history(history, user_name, score):
    """
    Добавляем в history.txt Имя и количество очков пользователя
    """
    with open(history, "a", encoding="utf-8") as file:
        history_info = [user_name, score]
        file.write(f"{history_info[0]} {history_info[1]} \n")
