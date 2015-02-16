word = input("Enter a word: ")
f = word 
n = input ("Enter number of words: ")
n = int(n)

count = 0
array = []
array2 = []
while count < n :
    m = input("enter word: " )
    array = array + [m]
    count+=1

for asd in array :
    if f in asd :
        array2=array2 + [f]
lenght_array2=len(array2)
print(lenght_array2)



    
