import re


def check_username_format(user):
    return re.match('^[A-Za-z-0-9]\@[A-Za-z]\.[A-Za-z]$', user)


def get_input():
    email = str(input())
    while not check_username_format(email):
        print('Email format is not correct. It should be like: "expression@string.string" ')
        email = str(input())
    password = str(input())
    return email, password


username, password = get_input()
