n = input("Please, enter a number: ")
n = int(n)

def perfect (number):
    is_perfect  = True
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
        is_perfect==True
        m = is_perfect
    else:
        is_perfect==False
    return m



arr = []
i = 6
while len(arr)< n :
    if perfect(i)==True :
        arr +=[i]
    i+=1
print(arr)
    
