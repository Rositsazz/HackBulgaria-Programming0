import re


def is_string_palindrom(string):
    string = str(string)
    string = re.sub('[!@#$%^&*()_+ ]', "", string)

    another_string = string[::-1]

    return string == another_string

# print(is_string_palindrom("kapak!!!!"))


def inner_trim(string):
    return " ".join(string.split())

# print(inner_trim("   ghf    !  dfds   "))


def sands_of_time(n):
    i = n
    j = 1
    while i > 0:
        string = "." * j
        string += "*" * i
        string += "." * j
        i -= 2
        j += 1
        print(string)

    i = 3
    j = j - 2
    while i <= n:
        string = "." * j
        string += i*"*"
        string += "." * j
        i += 2
        j -= 1
        print(string)

sands_of_time(7)
