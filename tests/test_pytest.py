import pytest
from main import top3_name, record_holders, same_name


def test_top3():
    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков",
         "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]

    expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    actual = top3_name(courses, mentors)
    assert expected == actual


def test_record_holders():
    expected = ('Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)\n'
                'Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)')
    actual = record_holders()
    assert expected == actual


def test_same_name():
    expected = ['На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, Максим Батырев, '
                'Максим Воронцов, Сергей Индюков, Сергей Сердюк',
                'На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, '
                'Александр Ульянцев, Александр Шлейко, Евгений Шек, Евгений Шмаргунов',
                'На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Иванов, '
                'Александр Ульянцев',
                'На курсе Frontend-разработчик с нуля есть тёзки: Александр Беспоясов, Александр Фитискин, '
                'Александр Шлейко']
    actual = same_name()
    assert expected == actual