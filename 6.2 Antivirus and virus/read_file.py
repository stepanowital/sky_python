#file = open("text.txt", "rb", ) # rt - read, binary

# file = open("text.txt", "rt")  # rt - read, text
#
# content = file.read()
# print(content)
#

#
# file.close()

# with open("guests.txt", "rt") as file:
#    guests_count = len(file.readlines())

    # for line in file:
    #     print(line)
# print(f"Количество гостей - {guests_count}")


with open("history.txt", encoding="utf-8") as file:
    games_count = 0
    max_score = 0
    for line in file:
        games_count += 1
        actual_score = line.split(" ")
        actual_score_int = int(actual_score[1])

        if actual_score_int > max_score:
            max_score = actual_score_int
    print(f"\nВсего игр сыграно: {games_count}")
    print(f"Максимальный рекорд: {max_score}")