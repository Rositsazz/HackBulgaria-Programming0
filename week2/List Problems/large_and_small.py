n = input("Enter number:")
n = int(n)
array = []

while n > 0 :
    num = n%10
    array = array + [num]
    n = n//10
#print(array)
    
min_number = sorted(array)
i = 0
string1 = ""
while i< len(min_number) :
    string1+=str(min_number[i])
    i+=1
print(string1)
max_number = sorted(array, reverse=True)
j = 0
string2 = ""
while j< len(max_number) :
    string2+=str(max_number[j])
    j+=1
print(string1)

print(string2)
    
    
