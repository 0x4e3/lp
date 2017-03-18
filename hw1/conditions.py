# coding=utf-8


def main(string_one, string_two):
    if string_one == string_two:
        return 1
    if len(string_one) > len(string_two):
        return 2
    if second_string == 'learn':
        return 3
    return 0


if __name__ == '__main__':
    first_string = input('Введите первую строку: ')
    second_string = input('Введите вторую строку: ')
    print(main(first_string, second_string))
