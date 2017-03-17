# coding=utf-8

def get_answer(question):
    answers = {
        "привет": "И тебе привет!",
        "как дела": "Лучше всех",
        "пока": "Увидимся",
    }
    answer = answers.get(question.lower(), "Даже не знаю, что тебе ответить")
    return answer


def indent_me_baby():
    x = 0
    while x < 10:
        print(x)
        x += 1


def main():
    # question = input("Спроси меня: ")
    # print(get_answer(question))
    indent_me_baby()


if __name__ == "__main__":
    main()
