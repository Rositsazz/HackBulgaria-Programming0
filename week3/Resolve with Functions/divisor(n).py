n = input("Please, enter a number: ")
n = int(n)

def divisor(number):

    m = number/2
    i = 1
    array = []

    while i<=m :

        if number%i==0 :
            array = array + [i]

        i+=1

    div = print(array)

    return div

divisor(n)
