def top3_name(courses, mentors):

    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[:3]

    return (f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: '
            f'{top_3[2][1]} раз(а)')


def record_holders():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков",
         "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "durations": duration}
        courses_list.append(course_dict)

    min_ = min(durations)
    max_ = max(durations)

    maxes = []
    minis = []
    for index, value in enumerate(durations):
        if value == max_:
            maxes.append(index)
        elif value == min_:
            minis.append(index)

    courses_min = []
    courses_max = []
    for id_ in minis:
        courses_min.append(courses_list[id_]["title"])
    for id_ in maxes:
        courses_max.append(
            courses_list[id_]["title"])

    return (f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_} месяца(ев)\nСамый длинный курс(ы): '
            f'{", ".join(courses_max)} - {max_} месяца(ев)')


def same_name():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков",
         "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    unique_names = sorted({name.split()[0] for course in courses_list for name in course["mentors"]})
    same_name_all = []

    for course in courses_list:
        same_name_list = []
        for name in unique_names:
            if [mentor_full_name.split()[0] for mentor_full_name in course["mentors"]].count(name) > 1:
                for full_name in course["mentors"]:
                    if name in full_name:
                        same_name_list.append(full_name)
        if same_name_list:
            same_name_all.append(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')

    return same_name_all
