# coding=utf-8

def str_concat(str_1, str_2):
    result = str(str_1) + str(str_2)
    print(result.upper())


def main():
    # user_info = {}.fromkeys(['first_name', 'last_name'])
    # user_info['first_name'] = input('Enter your first name: ')
    # user_info['last_name'] = input('Enter your last name: ')
    # print(user_info)
    str_concat('some_string', 'some_another_string')
    str_concat(1, 'some_another_string')
    str_concat(123, 4634.09)
    str_concat([2, 4, 34], 4634.09)
    str_concat({'a': 'asdf', 'b': 'asdfgc'}, 4634.09)
    

if __name__ == "__main__":
    main()
