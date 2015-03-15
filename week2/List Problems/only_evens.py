n = input("Enter number: ")
n = int(n)

even = []
count = 0

while count < n :

    m = input("enter number: " )
    m = int(m)

    if m%2==0 :
        even += [m]
    count += 1

lenght_of_evens = len(even)

print("Count of evens: " + str(lenght_of_evens))
print("Evens are:")

for even_number in even :
    print(even_number)
