number = input("Enter number: ")
number = int(number)


def reverse_int(n):
    string = ""
    while n != 0:
        string+=str(n%10)
        n = n//10
    return string

print(reverse_int(number))

def sum_digits(n):
    suma = 0
    while n != 0:
        suma+=n%10
        n = n//10
    return suma

print(sum_digits(number))

def product_digits(n):
    product = 1
    while n != 0:
        product*=n%10
        n = n//10
    return product

print (product_digits(number))
