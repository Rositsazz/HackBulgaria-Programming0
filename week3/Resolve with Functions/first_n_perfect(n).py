n = input("Please, enter a number: ")
n = int(n)

def perfect (number):

    is_perfect = False
    m = number/2
    i = 1
    array = []
    suma = 0

    while i<=m :
        if number%i==0 :
            array = array + [i]
        i+=1
    j = 0

    while j < len(array):
        suma=suma + array[j]
        j+=1

    if number==suma:
        is_perfect=True
    else :
        is_perfect=False

    return is_perfect

def first_n_perfect(number):

    arr = []
    i = 6
    while len(arr)< number :
        if perfect(i)==True :
            arr+=[i]
        i+=1
    s = arr

    return s

print(first_n_perfect(n))





