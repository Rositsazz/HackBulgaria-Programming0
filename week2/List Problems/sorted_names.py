n = input("Enter number:")
n = int(n)

count = 0
array = []
while count < n :
    m = input("enter word: " )
    array = array + [m]
    count+=1

print("Sorted names are:")
b = sorted(array)
i = 0
while i<len(b):
    print(b[i])
    i+=1

