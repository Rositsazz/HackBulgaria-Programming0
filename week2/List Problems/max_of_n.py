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
max_number = array[0]
i = 0
while i< len(array):
    if array[i]>max_number :
        max_number = array[i]
    i+=1
print("Max is: " + str(max_number))
