n = input("Enter number: ")
n = int(n)

count = 0
suma = 0
avg = 0
array = []
while count < n :
    m = input("enter number: " )
    m=int(m)
    array = array + [m]
    count+=1
    suma+=m
avg = suma / (len(array))
print("Avg is: " + str(avg))
