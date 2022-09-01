import json


def load_students(students_json):
    """ Загружает список студентов из файла """
    with open(students_json, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def load_professions(professions_json):
    """ Загружает список профессий из файла """
    with open(professions_json, "r", encoding="UTF-8") as professions:
        data = json.load(professions)

    return data


def get_student_by_pk(student_id, students):
    """ Получает словарь с данными студента по его pk """
    student_info = {}
    for student in students:
        if student['pk'] == student_id:
            student_info = student
    if student_info == {}:
        print("У нас нет такого студента")
        quit()

    return student_info


def get_profession_by_title(speciality, professions):
    """ Получает словарь с инфо о профе по названию """
    skills_pro = None
    for profession in professions:
        if profession['title'].lower() == speciality:
            skills_pro = profession['skills']
    if skills_pro is None:
        print("У нас нет такой специальности")
        quit()
    return skills_pro


def check_fitness(student_info, skills_pro):
    """ При получении данных студента и необходимой специальности
        возвращает словарь с информацией о соответствии данного студента"""
    student_info_set = set(student_info['skills'])
    skills_pro_set = set(skills_pro)

    has_to = list(student_info_set.intersection(skills_pro_set))
    lacks = list(skills_pro_set.difference(student_info_set))

    fit_percent = round((len(has_to) / len(skills_pro)) * 100)

    fitness = {
        "has": has_to,
        "lacks": lacks,
        "fit_percent": fit_percent
    }
    return fitness
