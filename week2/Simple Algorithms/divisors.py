n = input("Please, enter a number: ")
n = int(n)

m = n/2
i = 1
array = []
while i<=m :
    if n%i==0 :
        array = array + [i]
    i+=1
print(array)
