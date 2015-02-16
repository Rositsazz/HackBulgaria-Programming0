n = input("Enter number: ")
n = int(n)

count = 0
best = 0
array = []
while count < n :
    m = input("enter number: " )
    m=int(m)
    array = array + [m]
    count+=1
print(array)
min_number = array[0]
i = 0
while i< len(array):
    if array[i]<min_number :
        min_number = array[i]
    i+=1
print("Min is: " + str(min_number))
