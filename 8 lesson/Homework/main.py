if __name__ == '__main__':
    print("Игра начинается!")
    input()

    from Utils import Question, get_statistics
    import random
    import json

    questions_file = "questions.json"

    with open(questions_file, 'r', encoding="utf-8") as file:
        questions_data = json.load(file)

    random.shuffle(questions_data)

    questions = []
    for item in questions_data:
        text = item["q"]
        complexity = item["d"]
        correct_answer = item["a"]
        question = Question(text, complexity, correct_answer)
        questions.append(question)

    for question in questions:
        print(question.build_question())
        question.user_answer = input("\nВаш ответ: ")
        print(question.build_feedback())

    print(get_statistics(questions))
