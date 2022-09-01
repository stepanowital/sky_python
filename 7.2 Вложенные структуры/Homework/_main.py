if __name__ == "__main__":
    from functions import *

    students_json = "students.json"
    professions_json = "professions.json"

    # Запрос номера студента
    student_id = int(input("Введите номер студента:\n"))

    # Функция для загрузки списка студентов в файл
    students = load_students(students_json)

    # Функция для загрузки списка профессий в файл
    professions = load_professions(professions_json)

    # Информация о студенте по его номеру
    student_info = get_student_by_pk(student_id, students)

    print(f"Студент {student_info['full_name']}".rjust(30, '*'))
    print(f"Знает {', '.join(student_info['skills'])}".rjust(30, '*'))
    print(f"Выберите специальность для оценки студента {student_info['full_name']}".rjust(30, '*'))
    speciality = input().lower()

    # Получение словаря с инфо о профе по названию
    skills_pro = get_profession_by_title(speciality, professions)

    # Получение словаря с информацией о соответствии данного студента
    fitness = check_fitness(student_info, skills_pro)

    print(f"Пригодность {fitness['fit_percent']}%".rjust(30, '*'))
    print(f"{student_info['full_name']} знает {', '.join(fitness['has'])}".rjust(30, '*'))
    print(f"{student_info['full_name']} не знает {', '.join(fitness['lacks'])}".rjust(30, '*'))
