n = input("Enter number: ")
n = int(n)

def to_digits(number):
    array = []
    while number > 0:
        m = number%10
        array +=[m]
        number = number//10

    digits = print(array)
    return digits

def is_prime_number (number):
    start = 2
    is_prime = True
    if number == 1:
        is_prime = False
    while start < n:
        if number % start == 0:
            is_prime = False
            break
        start = start + 1
    return print(is_prime)

to_digits(n)
is_prime_number(n)
