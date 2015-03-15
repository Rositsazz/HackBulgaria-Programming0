n = input("Please, enter a number: ")
n = int(n)

def sum_ints(number):

    m = number/2
    i = 1
    suma = 0
    array = []

    while i<=m :
        if number%i==0 :
            array = array + [i]
        i+=1

    j = 0

    while j < len(array):
        suma+=array[j]
        j+=1

    sum_of_divisors = print(suma)

    return sum_of_divisors


sum_ints(n)
