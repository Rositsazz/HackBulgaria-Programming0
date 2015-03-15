n = input("Please, enter a number: ")
n = int(n)

m = n/2
i = 1
array = []
suma = 0

while i<=m :
    if n%i==0 :
        array += [i]

    i+=1

print(array)

j = 0
while j < len(array):
    suma += array[j]
    j+=1

print(suma)
