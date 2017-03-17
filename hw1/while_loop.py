# coding=utf-8
"""
To use this script, do not forget to run
    export PYTHONPATH=PYTHONPATH:./
in the ~/Projects/personal/learn_python directory.
"""
from lesson1.answers import get_answer

persons = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(name):
    iterations = 0
    while persons:
        iterations += 1
        current_person = persons.pop(0)
        if current_person == name:
            print('{} нашелся с {} попытки!'.format(name, iterations))
            return
    print('В списке известных людей {} отсутствует'.format(name))


def ask_user():
    phrase = None
    while phrase != 'хорошо':
        phrase = input('Как дела? — ')
        print(get_answer(phrase))
        if phrase == 'пока':
            break

def talk_to_me():
    try:
        ask_user()
    except KeyboardInterrupt:
        print('\nПока-пока!')


def main():
    # required_person_name = input('Введите имя искомого персонажа: ')
    # find_person(required_person_name)
    talk_to_me()


if __name__ == "__main__":
    main()
