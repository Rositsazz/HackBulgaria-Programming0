n = input("Enter number: ")
n = int(n)

array = []

while n > 0:
    m = n%10
    array +=[m]
    n = n//10

print(array)
i = 0
is_prime = True
while i < len(array):
    if array[i] in [2,3,5,7] :
        is_prime = True
        break
    else :
        is_prime = False        
    i+=1

print(is_prime)
