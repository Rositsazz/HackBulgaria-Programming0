n = input("Please, enter a number: ")
n = int(n)

m = n/2
i = 1
array = []
suma = 0
while i<=m :
    if n%i==0 :
        array = array + [i]

    i+=1

print(array)
j = 0
while j < len(array):
    suma=suma + array[j]
    j+=1

print(suma)

if n==suma:
    print("The number is perfect")
else:
    print("The number is not perfect")
