n = input("Please, enter a number: ")
n = int(n)

def is_perfect(number):
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

    if number==suma:
        a = print("The number is perfect")
    else:
        b = print("The number is not perfect")
    return a

is_perfect(n)
